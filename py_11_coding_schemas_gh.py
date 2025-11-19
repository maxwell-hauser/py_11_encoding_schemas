#!/usr/bin/env python3
"""
Chapter 11: Coding Schemas (ASCII, Unicode)
Demonstrates character encoding standards
"""

def char_to_ascii(char):
    """Get ASCII value of a character"""
    return ord(char)

def ascii_to_binary(char):
    """Convert character to 7-bit ASCII binary"""
    ascii_val = ord(char)
    if ascii_val > 127:
        raise ValueError(f"Character '{char}' is not in ASCII range (0-127)")
    return format(ascii_val, '07b')

def ascii_to_8bit(char):
    """Convert character to 8-bit ASCII (with parity bit space)"""
    ascii_val = ord(char)
    return format(ascii_val, '08b')

def string_to_ascii(text):
    """Convert string to ASCII representation"""
    return [(char, ord(char), ascii_to_8bit(char)) for char in text]

def char_to_unicode(char):
    """Get Unicode code point"""
    return f"U+{ord(char):04X}"

def display_ascii_table(start=32, end=127):
    """Display ASCII table for printable characters"""
    print("\nDec | Hex | Binary   | Char")
    print("----|-----|----------|------")
    
    for i in range(start, min(end + 1, 128)):
        char = chr(i)
        if i < 32 or i == 127:
            char = f"<{char}>"  # Control character
        binary = format(i, '08b')
        print(f"{i:3d} | {i:02X}  | {binary} | {char}")

def main():
    print("=" * 60)
    print("CHAPTER 11: Coding Schemas (ASCII and Unicode)")
    print("=" * 60)
    
    # Example 1: ASCII encoding
    print("\n--- Example 1: ASCII Encoding ---")
    word = "HELLO"
    print(f"Word: {word}\n")
    print("Char | ASCII | Binary (8-bit)")
    print("-----|-------|---------------")
    
    for char in word:
        ascii_val = char_to_ascii(char)
        binary = ascii_to_8bit(char)
        print(f"  {char}  |  {ascii_val:3d}  | {binary}")
    
    # Complete representation
    complete_binary = ' '.join(ascii_to_8bit(c) for c in word)
    print(f"\nComplete binary: {complete_binary}")
    
    # Example 2: ASCII Character Ranges
    print("\n--- Example 2: ASCII Character Ranges ---")
    print("\nControl Characters (0-31, 127):")
    control_examples = [
        (0, "NUL (Null)"),
        (1, "SOH (Start of Heading)"),
        (7, "BEL (Bell)"),
        (10, "LF (Line Feed)"),
        (13, "CR (Carriage Return)"),
        (27, "ESC (Escape)"),
        (127, "DEL (Delete)")
    ]
    
    for code, description in control_examples:
        binary = format(code, '08b')
        print(f"  {code:3d} (0x{code:02X}): {binary} - {description}")
    
    print("\nPrintable Characters (32-126):")
    print("  32-47:  Space and punctuation")
    print("  48-57:  Digits (0-9)")
    print("  65-90:  Uppercase letters (A-Z)")
    print("  97-122: Lowercase letters (a-z)")
    
    # Example 3: Partial ASCII Table
    print("\n--- Example 3: Printable ASCII Characters ---")
    
    # Digits
    print("\nDigits:")
    print("Char | Dec | Hex | Binary")
    print("-----|-----|-----|--------")
    for i in range(48, 58):  # 0-9
        print(f"  {chr(i)}  | {i:3d} | {i:02X}  | {format(i, '08b')}")
    
    # Uppercase letters (sample)
    print("\nUppercase (sample):")
    print("Char | Dec | Hex | Binary")
    print("-----|-----|-----|--------")
    for i in range(65, 72):  # A-G
        print(f"  {chr(i)}  | {i:3d} | {i:02X}  | {format(i, '08b')}")
    
    # Example 4: ASCII to Unicode
    print("\n--- Example 4: ASCII to Unicode Conversion ---")
    print("\nASCII range: 0x00 to 0x7F")
    print("Unicode range: U+0000 to U+007F")
    print("\nASCII values map directly to Unicode:")
    
    test_chars = ['A', 'Z', '0', '9', ' ']
    print("\nChar | ASCII Hex | Unicode")
    print("-----|-----------|--------")
    for char in test_chars:
        ascii_hex = format(ord(char), '02X')
        unicode_val = char_to_unicode(char)
        print(f"  {char}  |    0x{ascii_hex}   | {unicode_val}")
    
    # Example 5: Extended ASCII
    print("\n--- Example 5: Extended ASCII (8-bit) ---")
    print("\nExtended ASCII uses all 8 bits: 256 characters (0-255)")
    print("  0-127:   Standard ASCII")
    print("  128-255: Extended characters")
    print("\nExtended characters include:")
    print("  • Accented letters (é, ñ, ü)")
    print("  • Special symbols (©, °, ±)")
    print("  • Box drawing characters")
    print("  • Greek letters (α, β, γ)")
    
    # Example 6: Unicode overview
    print("\n--- Example 6: Unicode Encoding ---")
    print("\nUnicode: Universal character encoding")
    print("  Uses 16+ bits (compared to ASCII's 7 bits)")
    print("  Can represent 65,536+ characters")
    print("  Format: U+XXXX (hexadecimal)")
    
    print("\nUnicode Blocks (examples):")
    blocks = [
        ("U+0000 - U+007F", "Basic Latin (ASCII)"),
        ("U+0080 - U+00FF", "Latin-1 Supplement"),
        ("U+0370 - U+03FF", "Greek and Coptic"),
        ("U+0590 - U+05FF", "Hebrew"),
        ("U+0600 - U+06FF", "Arabic"),
        ("U+4E00 - U+9FFF", "CJK Unified Ideographs")
    ]
    
    for range_str, description in blocks:
        print(f"  {range_str}: {description}")
    
    # Example 7: Character encoding comparison
    print("\n--- Example 7: Encoding Comparison ---")
    
    test_char = 'B'
    print(f"\nCharacter: {test_char}")
    print(f"ASCII decimal:   {ord(test_char)}")
    print(f"ASCII hex:       0x{ord(test_char):02X}")
    print(f"ASCII binary:    {format(ord(test_char), '08b')}")
    print(f"Unicode:         {char_to_unicode(test_char)}")
    
    # Example 8: Real-world application
    print("\n--- Example 8: Practical Example ---")
    message = "Hello123"
    print(f"\nMessage: '{message}'")
    print(f"Length: {len(message)} characters")
    print(f"Storage (ASCII): {len(message) * 8} bits = {len(message)} bytes")
    
    print("\nDetailed breakdown:")
    ascii_data = string_to_ascii(message)
    for char, ascii_val, binary in ascii_data:
        print(f"  '{char}' → {ascii_val:3d} → {binary}")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- ASCII: 7-bit encoding (0-127), 128 characters")
    print("- Extended ASCII: 8-bit (0-255), 256 characters")
    print("- Unicode: 16+ bit, supports all languages")
    print("- ASCII codes 0-31 and 127 are control characters")
    print("- ASCII 32-126 are printable characters")
    print("- Unicode U+0000 to U+007F = ASCII")
    print("=" * 60)

if __name__ == "__main__":
    main()
