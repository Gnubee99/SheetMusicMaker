# SheetMusicMaker 🎹

Create printable sheet music based on input provided by virtualpiano files.

## Features

- ✨ Convert Virtual Piano notation to professional-quality sheet music
- 🎵 Support for multiple octaves (lowercase, uppercase, and numbers)
- 🎼 **Professional music notation rendering:**
  - Proper staff lines with treble clef
  - Time signatures (4/4, 3/4, 2/4, 6/8)
  - Key signatures
  - Measure grouping with bar lines
  - Double bar line at the end
  - Automatic rest insertion for incomplete measures
  - Note durations (quarter, half, whole notes)
  - Sharp accidentals (♯)
  - Ledger lines for notes outside the staff
- 🎹 **Grand Staff support:** Dual staff (treble + bass clef) for piano music
- 📝 **Customization options:**
  - Add title and subtitle to your sheet music
  - Choose page size (A4 or Letter)
  - Select time signature
- 🎶 **Chord support:** Play multiple notes simultaneously using square brackets
- 📄 Export to PDF for printing
- 🖼️ Export to PNG image format
- 🎨 Beautiful, responsive web interface
- ⚡ No installation required - works directly in your browser

## How to Use

1. **Open the Application**
   - Simply open `index.html` in any modern web browser
   - Or visit the hosted version (if deployed)

2. **Configure Music Settings (Optional)**
   - Enter a title for your piece
   - Add a subtitle (composer name, etc.)
   - Select time signature (4/4, 3/4, 2/4, or 6/8)
   - Choose page size for printing (A4 or Letter)
   - Enable Grand Staff mode for piano music with both treble and bass clefs

3. **Enter Virtual Piano Notation**
   - Type or paste Virtual Piano notation in the text area
   - Use lowercase letters (a-z) for middle octave notes
   - Use uppercase letters (A-Z) for sharps or higher octaves
   - Use numbers (1-9, 0) for lower octave notes
   - Use spaces to separate notes for quarter note duration
   - Use `|` after a note for half note duration
   - Use ` | ` (with spaces) after a note for whole note duration
   - Use square brackets `[tyu]` to create chords

4. **Generate Sheet Music**
   - Click the "Generate Sheet Music" button
   - Your notation will be converted to standard music notation with proper measures
   - The sheet music will display below the input area

5. **Export Your Music**
   - Click "Download PDF" to save as a printable PDF
   - Click "Download Image" to save as a PNG image

## Virtual Piano Key Mapping

### Lower Octave (C2-B3)
- White keys: `1 2 3 4 5 6 7 8 9 0 q w e r`
- Black keys (sharps): `! @ $ % ^ * ( Q W E`

### Middle Octave (C4-D5)
- White keys: `t y u i o p a s d`
- Black keys (sharps): `T Y I O P S D`

### Upper Octave (E5-C7)
- White keys: `f g h j k l z x c v b n m`
- Black keys (sharps): `G H J L Z C B`

## Example Inputs

Try these examples to get started:

```
t y u i o p a s d
```
Simple melody in C major

```
[tyu] [iop] [asd]
```
Chord progression

```
t y| u i| o p| a
```
Half notes with bar lines

```
t y u | i o p | a s d
```
Whole notes with proper measures

```
1 2 3 4 5 t y u i o
```
Lower and middle octave combination (use Grand Staff mode)

## Technical Details

- Built with HTML, CSS, and JavaScript
- Enhanced custom SVG rendering engine for professional music notation
- Implements proper music theory:
  - Time signature-based measure grouping
  - Automatic rest insertion for incomplete measures
  - Note duration spacing and rendering
  - Grand staff with brace for piano music
  - Proper accidental placement
- Uses browser's XMLSerializer and Canvas API for image export
- Uses window.print() for PDF generation with page size support
- No backend required - runs entirely in the browser

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

## Development

This is a single-page application. To modify:
1. Edit `index.html`
2. The JavaScript code is embedded in the HTML file
3. Refresh your browser to see changes

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

MIT License - feel free to use and modify as needed.

## Credits

- Custom SVG music notation implementation
- Virtual Piano community for the notation system

## How to play
SEMANTICS OF MUSIC SHEETS
Here is a simple explanation of how to easily play the Virtual Piano Music Sheets

ORDER OF LETTERS  HOW THEY’RE PLAYED
`[asdf]`            Play notes together simultaneously
`[a s d f]`         Play the sequence at fastest possible speed
`asdf`              Play notes one after the other quickly
`a s d f`           Play each note after a short pause
`[as] [df]`         Play “as” together, short pause, then “df” together
`as|df`             Pause for “|”
`as| df`            Long pause for “|” with one extra space
`as | df`           Longer pause for “|” with 2 extra spaces
`as| |df`           Longest pause for 2 “|” with an extra space
`Paragraph Break`   Extended pause