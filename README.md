# SheetMusicMaker
Create printable sheet music based on input provided by virtualpiano files

## Key Mappings

### Lower Octave (C2-B3)
- **White keys**: `1 2 3 4 5 6 7 8 9 0 q w e r`
- **Black keys (sharps)**: `! @ $ % ^ * ( Q W E`

### Middle Octave (C4-D5)
- **White keys**: `t y u i o p a s d`
- **Black keys (sharps)**: `T Y I O P S D`

### Upper Octave (E5-C7)
- **White keys**: `f g h j k l z x c v b n m`
- **Black keys (sharps)**: `G H J L Z C B`

## Note Timing Patterns

The spacing and formatting of letters determines how they are played:

| Pattern | Example | Description |
|---------|---------|-------------|
| `[asdf]` | `[asdf]` | Play notes together simultaneously |
| `[a s d f]` | `[a s d f]` | Play the sequence at fastest possible speed |
| `asdf` | `asdf` | Play notes one after the other quickly |
| `a s d f` | `a s d f` | Play each note after a short pause |
| `[as] [df]` | `[as] [df]` | Play "as" together, short pause, then "df" together |
| `as|df` | `as|df` | Pause for "\|" |
| `as| df` | `as| df` | Long pause for "\|" with one extra space |
| `as | df` | `as | df` | Longer pause for "\|" with 2 extra spaces |
| `as| |df` | `as| |df` | Longest pause for 2 "\|" with an extra space |
| Paragraph Break | (empty line) | Extended pause |

## Usage

Run the script to see examples of how the key mappings work:

```bash
python3 sheet_music_maker.py
```

The script will display all key mappings and demonstrate the various timing patterns.

## Example

```python
from sheet_music_maker import SheetMusicMaker

maker = SheetMusicMaker()

# Parse some input
input_text = "[ty] [ui] o p| |[as]"
notes = maker.parse_input(input_text)
output = maker.format_output(notes)
print(output)
```

This will parse the input and convert it to musical notation with appropriate timing information.
