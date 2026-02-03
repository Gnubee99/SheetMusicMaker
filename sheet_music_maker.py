#!/usr/bin/env python3
"""
Sheet Music Maker - Convert keyboard input to musical notes
Supports three octaves with specific key mappings
"""

import re
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Note:
    """Represents a musical note with timing information"""
    key: str
    note_name: str
    octave: int
    duration: str  # 'short', 'normal', 'long'
    simultaneous_group: int = 0  # 0 means not in a group


class SheetMusicMaker:
    def __init__(self):
        # Lower Octave (C2-B3) mappings
        self.lower_white_keys = {
            '1': ('C', 2), '2': ('D', 2), '3': ('E', 2), '4': ('F', 2),
            '5': ('G', 2), '6': ('A', 2), '7': ('B', 2), '8': ('C', 3),
            '9': ('D', 3), '0': ('E', 3), 'q': ('F', 3), 'w': ('G', 3),
            'e': ('A', 3), 'r': ('B', 3)
        }
        self.lower_black_keys = {
            '!': ('C#', 2), '@': ('D#', 2), '$': ('F#', 2), '%': ('G#', 2),
            '^': ('A#', 2), '*': ('C#', 3), '(': ('D#', 3), 'Q': ('F#', 3),
            'W': ('G#', 3), 'E': ('A#', 3)
        }
        
        # Middle Octave (C4-D5) mappings
        self.middle_white_keys = {
            't': ('C', 4), 'y': ('D', 4), 'u': ('E', 4), 'i': ('F', 4),
            'o': ('G', 4), 'p': ('A', 4), 'a': ('B', 4), 's': ('C', 5),
            'd': ('D', 5)
        }
        self.middle_black_keys = {
            'T': ('C#', 4), 'Y': ('D#', 4), 'I': ('F#', 4), 'O': ('G#', 4),
            'P': ('A#', 4), 'S': ('C#', 5), 'D': ('D#', 5)
        }
        
        # Upper Octave (E5-C7) mappings
        self.upper_white_keys = {
            'f': ('E', 5), 'g': ('F', 5), 'h': ('G', 5), 'j': ('A', 5),
            'k': ('B', 5), 'l': ('C', 6), 'z': ('D', 6), 'x': ('E', 6),
            'c': ('F', 6), 'v': ('G', 6), 'b': ('A', 6), 'n': ('B', 6),
            'm': ('C', 7)
        }
        self.upper_black_keys = {
            'G': ('F#', 5), 'H': ('G#', 5), 'J': ('A#', 5), 'L': ('C#', 6),
            'Z': ('D#', 6), 'C': ('F#', 6), 'B': ('A#', 6)
        }
        
        # Combine all mappings
        self.key_to_note = {}
        self.key_to_note.update(self.lower_white_keys)
        self.key_to_note.update(self.lower_black_keys)
        self.key_to_note.update(self.middle_white_keys)
        self.key_to_note.update(self.middle_black_keys)
        self.key_to_note.update(self.upper_white_keys)
        self.key_to_note.update(self.upper_black_keys)
    
    def parse_input(self, text: str) -> List[List[Note]]:
        """
        Parse input text and convert to notes with timing information
        
        Rules:
        - [asdf]: Play notes together simultaneously
        - [a s d f]: Play the sequence at fastest possible speed
        - asdf: Play notes one after the other quickly
        - a s d f: Play each note after a short pause
        - [as] [df]: Play "as" together, short pause, then "df" together
        - as|df: Pause for "|"
        - as| df: Long pause for "|" with one extra space
        - as | df: Longer pause for "|" with 2 extra spaces
        - as| |df: Longest pause for 2 "|" with an extra space
        - Paragraph Break: Extended pause
        """
        paragraphs = text.split('\n\n')
        result = []
        
        for para_idx, paragraph in enumerate(paragraphs):
            if not paragraph.strip():
                continue
                
            # Process each paragraph
            para_notes = self._parse_paragraph(paragraph)
            result.extend(para_notes)
            
            # Add extended pause between paragraphs (except last)
            if para_idx < len(paragraphs) - 1:
                result.append([])  # Empty list represents paragraph break
        
        return result
    
    def _parse_paragraph(self, text: str) -> List[List[Note]]:
        """Parse a single paragraph of text"""
        result = []
        
        # First check if there are no pipes - if so, handle the simple case
        if '|' not in text:
            # Process the entire text as one part
            result.extend(self._parse_text_part(text))
            return result
        
        # Split by pipe symbols while preserving spacing context
        parts = re.split(r'(\|+)', text)
        
        for i, part in enumerate(parts):
            if not part or part.strip() == '':
                continue
            
            # Check if this is a pipe symbol
            if re.match(r'\|+', part):
                # Count pipes and surrounding spaces
                pipe_count = len(part)
                prev_space = len(parts[i-1]) - len(parts[i-1].rstrip()) if i > 0 else 0
                next_space = len(parts[i+1]) - len(parts[i+1].lstrip()) if i < len(parts)-1 else 0
                
                # Create pause note based on spacing
                pause_length = 'short'
                if pipe_count > 1 or (prev_space > 0 and next_space > 0):
                    pause_length = 'longest'
                elif prev_space > 0 or next_space > 0:
                    if prev_space + next_space > 1:
                        pause_length = 'longer'
                    else:
                        pause_length = 'long'
                
                result.append([Note('|', 'PAUSE', 0, pause_length)])
                continue
            
            # Process notes
            result.extend(self._parse_text_part(part.strip()))
        
        return result
    
    def _parse_text_part(self, text: str) -> List[List[Note]]:
        """Parse a text part (between pipes or entire paragraph)"""
        result = []
        
        # Check for bracketed groups [asdf] or [a s d f]
        bracket_pattern = r'\[([^\]]+)\]'
        
        # Split into tokens (bracketed and non-bracketed)
        tokens = re.split(bracket_pattern, text)
        
        for token in tokens:
            if not token or not token.strip():
                continue
            
            # Check if this was inside brackets
            is_bracketed = '[' + token + ']' in text or token in re.findall(bracket_pattern, text)
            
            if is_bracketed:
                # Bracketed group - check for spaces
                if ' ' in token:
                    # [a s d f] - fastest sequence
                    notes = self._parse_notes(token, 'fastest')
                    if notes:
                        result.append(notes)
                else:
                    # [asdf] - simultaneous
                    notes = self._parse_notes(token, 'simultaneous')
                    if notes:
                        result.append(notes)
            else:
                # Not bracketed - check for spaces
                if ' ' in token:
                    # a s d f - short pause between each
                    # Split by spaces - each part is either a single key or a group of keys
                    keys = token.split()
                    for key_group in keys:
                        if len(key_group) == 1:
                            # Single key - play with pause
                            notes = self._parse_notes(key_group, 'short_pause')
                            if notes:
                                result.append(notes)
                        else:
                            # Multiple keys together - play quickly
                            notes = self._parse_notes(key_group, 'quick')
                            if notes:
                                result.append(notes)
                else:
                    # asdf - quick succession
                    notes = self._parse_notes(token, 'quick')
                    if notes:
                        result.append(notes)
        
        return result
    
    def _parse_notes(self, keys: str, timing: str) -> List[Note]:
        """Convert a string of keys to Note objects with given timing"""
        notes = []
        
        # Handle different timing types
        if timing == 'simultaneous':
            # All notes play together
            for i, key in enumerate(keys.strip().replace(' ', '')):
                if key in self.key_to_note:
                    note_name, octave = self.key_to_note[key]
                    notes.append(Note(key, note_name, octave, 'normal', simultaneous_group=1))
        
        elif timing == 'fastest':
            # Fast sequence (inside brackets with spaces)
            for key in keys.split():
                if key in self.key_to_note:
                    note_name, octave = self.key_to_note[key]
                    notes.append(Note(key, note_name, octave, 'fastest'))
        
        elif timing == 'quick':
            # Quick succession (no spaces, no brackets)
            for key in keys:
                if key in self.key_to_note:
                    note_name, octave = self.key_to_note[key]
                    notes.append(Note(key, note_name, octave, 'quick'))
        
        elif timing == 'short_pause':
            # With pauses between (spaces, no brackets)
            # This is called for single keys only
            for key in keys:
                if key in self.key_to_note:
                    note_name, octave = self.key_to_note[key]
                    notes.append(Note(key, note_name, octave, 'short_pause'))
        
        return notes
    
    def format_output(self, notes: List[List[Note]]) -> str:
        """Format parsed notes as a readable output"""
        output = []
        
        for group in notes:
            if not group:
                output.append("--- PARAGRAPH BREAK ---")
                continue
            
            if group[0].note_name == 'PAUSE':
                pause_type = group[0].duration
                output.append(f"--- PAUSE ({pause_type}) ---")
                continue
            
            # Check if simultaneous
            if group[0].simultaneous_group > 0:
                note_str = " + ".join([f"{n.note_name}{n.octave}" for n in group])
                output.append(f"[{note_str}] (simultaneous)")
            else:
                timing_labels = {
                    'fastest': 'fastest',
                    'quick': 'quick',
                    'short_pause': 'with pause',
                    'normal': 'normal'
                }
                for note in group:
                    label = timing_labels.get(note.duration, note.duration)
                    output.append(f"{note.note_name}{note.octave} ({label})")
        
        return '\n'.join(output)
    
    def print_key_mappings(self):
        """Print all key mappings for reference"""
        print("=== Sheet Music Maker Key Mappings ===\n")
        
        print("Lower Octave (C2-B3):")
        print("  White keys: 1 2 3 4 5 6 7 8 9 0 q w e r")
        print("  Black keys: ! @ $ % ^ * ( Q W E")
        print()
        
        print("Middle Octave (C4-D5):")
        print("  White keys: t y u i o p a s d")
        print("  Black keys: T Y I O P S D")
        print()
        
        print("Upper Octave (E5-C7):")
        print("  White keys: f g h j k l z x c v b n m")
        print("  Black keys: G H J L Z C B")
        print()
        
        print("Timing/Spacing Rules:")
        print("  [asdf]        Play notes together simultaneously")
        print("  [a s d f]     Play the sequence at fastest possible speed")
        print("  asdf          Play notes one after the other quickly")
        print("  a s d f       Play each note after a short pause")
        print("  [as] [df]     Play 'as' together, short pause, then 'df' together")
        print("  as|df         Pause for '|'")
        print("  as| df        Long pause for '|' with one extra space")
        print("  as | df       Longer pause for '|' with 2 extra spaces")
        print("  as| |df       Longest pause for 2 '|' with an extra space")
        print("  Paragraph     Extended pause")
        print()


def main():
    """Example usage"""
    maker = SheetMusicMaker()
    
    # Print mappings
    maker.print_key_mappings()
    
    # Example input
    print("\n=== Example Usage ===\n")
    
    # Test various patterns
    test_inputs = [
        "[asdf]",
        "[a s d f]",
        "asdf",
        "a s d f",
        "[ty] [ui]",
        "ty|ui",
        "ty| ui",
        "ty | ui",
        "123 456\n\n789 0qw"
    ]
    
    for test_input in test_inputs:
        print(f"Input: {repr(test_input)}")
        notes = maker.parse_input(test_input)
        output = maker.format_output(notes)
        print(output)
        print()


if __name__ == "__main__":
    main()
