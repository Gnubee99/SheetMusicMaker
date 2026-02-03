# SheetMusicMaker 🎹

Create printable sheet music based on input provided by virtualpiano files.

## Features

- ✨ Convert Virtual Piano notation to Western sheet music
- 🎵 Support for multiple octaves (lowercase, uppercase, and numbers)
- 📄 Export to PDF for printing
- 🖼️ Export to PNG image format
- 🎨 Beautiful, responsive web interface
- ⚡ No installation required - works directly in your browser

## How to Use

1. **Open the Application**
   - Simply open `index.html` in any modern web browser
   - Or visit the hosted version (if deployed)

2. **Enter Virtual Piano Notation**
   - Type or paste Virtual Piano notation in the text area
   - Use lowercase letters (a-z) for middle octave notes
   - Use uppercase letters (A-Z) for sharps or higher octaves
   - Use numbers (1-9, 0) for lower octave notes
   - Separate notes with spaces
   - Optionally use `|` to create measure breaks

3. **Generate Sheet Music**
   - Click the "Generate Sheet Music" button
   - Your notation will be converted to standard music notation
   - The sheet music will display below the input area

4. **Export Your Music**
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
a s d f g f d s a
```
Simple C major scale pattern

```
q w e r t y u i o p
```
Upper octave sequence

```
a s d | f g h | j k l
```
With measure breaks

## Technical Details

- Built with HTML, CSS, and JavaScript
- Uses native SVG rendering for music notation
- Uses browser's XMLSerializer and Canvas API for image export
- Uses window.print() for PDF generation
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