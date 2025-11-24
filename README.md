# Chapter 11: Coding Schemas (ASCII and Unicode)

## Overview

This chapter covers character encoding standards—methods for representing text characters as binary numbers. Understanding ASCII and Unicode is essential for text processing, data transmission, and international computing.

## Key Concepts

### What is Character Encoding?

**Definition:** A system that maps characters (letters, numbers, symbols) to numeric codes that computers can store and process.

```
Character → Numeric Code → Binary Representation
   'A'    →      65      →    01000001
```

## ASCII (American Standard Code for Information Interchange)

### ASCII Basics

- **Standard:** ANSI X3.4-1968
- **Bit Width:** 7 bits (0-127) or 8 bits (0-255 with extended)
- **Characters:** 128 standard characters
- **Purpose:** English language and basic symbols

### ASCII Character Ranges

```
0-31:    Control characters (non-printable)
32-47:   Special characters and space
48-57:   Digits '0'-'9'
58-64:   Special characters
65-90:   Uppercase letters 'A'-'Z'
91-96:   Special characters
97-122:  Lowercase letters 'a'-'z'
123-127: Special characters
```

### Standard ASCII Table (0-127)

#### Control Characters (0-31)
```
Dec  Hex  Char  Name
0    00   NUL   Null
7    07   BEL   Bell
8    08   BS    Backspace
9    09   HT    Horizontal Tab
10   0A   LF    Line Feed (newline)
13   0D   CR    Carriage Return
27   1B   ESC   Escape
32   20   SP    Space
```

#### Printable Characters (32-126)

**Digits:**
```
'0' = 48 (0x30) = 0011 0000
'1' = 49 (0x31) = 0011 0001
...
'9' = 57 (0x39) = 0011 1001
```

**Uppercase Letters:**
```
'A' = 65 (0x41) = 0100 0001
'B' = 66 (0x42) = 0100 0010
...
'Z' = 90 (0x5A) = 0101 1010
```

**Lowercase Letters:**
```
'a' = 97  (0x61) = 0110 0001
'b' = 98  (0x62) = 0110 0010
...
'z' = 122 (0x7A) = 0111 1010
```

**Special Characters:**
```
'!' = 33  (0x21)    '@' = 64  (0x40)
'#' = 35  (0x23)    '[' = 91  (0x5B)
'$' = 36  (0x24)    ']' = 93  (0x5D)
'%' = 37  (0x25)    '{' = 123 (0x7B)
'&' = 38  (0x26)    '}' = 125 (0x7D)
```

### Extended ASCII (128-255)

- **8th bit activated:** Extends to 256 characters
- **Non-standard:** Different code pages for different languages
- **Code Page 437:** Original IBM PC
- **ISO-8859-1 (Latin-1):** Western European languages
- **Problem:** Incompatible between systems

### ASCII Properties and Patterns

#### Case Conversion
```
Uppercase to lowercase: Add 32 (flip bit 5)
'A' (65)  = 0100 0001
'a' (97)  = 0110 0001  (65 + 32)
          
Lowercase to uppercase: Subtract 32 (flip bit 5)
```

#### Digit to Numeric Value
```
'5' (53) → 5:  Subtract 48 (or AND with 0x0F)
53 - 48 = 5
0011 0101 AND 0000 1111 = 0000 0101 (5)
```

## Unicode

### Unicode Basics

- **Purpose:** Universal character set for all languages
- **Range:** 0 to 1,114,111 (0x10FFFF)
- **Characters:** Over 149,000 assigned (as of Unicode 15.0)
- **Includes:** All scripts, symbols, emojis, mathematical symbols

### Unicode Encoding Forms

#### 1. UTF-8 (Variable Length: 1-4 bytes)
- **Most common on web and Unix/Linux**
- **Backward compatible with ASCII**
- **1 byte:** 0-127 (same as ASCII)
- **2 bytes:** 128-2,047
- **3 bytes:** 2,048-65,535
- **4 bytes:** 65,536-1,114,111

**Example:**
```
'A' (U+0041) → 01000001 (1 byte, same as ASCII)
'é' (U+00E9) → 11000011 10101001 (2 bytes)
'中' (U+4E2D) → 11100100 10111000 10101101 (3 bytes)
'😀' (U+1F600) → 11110000 10011111 10011000 10000000 (4 bytes)
```

#### 2. UTF-16 (Variable Length: 2 or 4 bytes)
- **Used by Windows, Java, JavaScript**
- **2 bytes:** Most common characters (BMP)
- **4 bytes:** Supplementary characters (surrogates)

**Example:**
```
'A' (U+0041) → 0041 (2 bytes)
'😀' (U+1F600) → D83D DE00 (4 bytes, surrogate pair)
```

#### 3. UTF-32 (Fixed Length: 4 bytes)
- **Simple:** Each character is exactly 4 bytes
- **Inefficient:** Wastes space
- **Rarely used** except for internal processing

### Unicode Code Points

**Notation:** U+XXXX (hex)

```
U+0041 → 'A' (Latin capital A)
U+03B1 → 'α' (Greek lowercase alpha)
U+4E2D → '中' (Chinese character)
U+1F600 → '😀' (Grinning face emoji)
```

### Unicode Planes

```
Plane 0 (BMP): U+0000 to U+FFFF (Basic Multilingual Plane)
  - Most common characters
  - Latin, Greek, Cyrillic, Arabic, Chinese, Japanese, etc.

Plane 1 (SMP): U+10000 to U+1FFFF (Supplementary Multilingual Plane)
  - Historic scripts, musical symbols, emojis

Planes 2-16: Additional supplementary planes
```

## ASCII vs Unicode Comparison

| Feature | ASCII | Unicode |
|---------|-------|---------|
| **Bit Width** | 7/8 bits | Variable (8-32 bits) |
| **Characters** | 128/256 | 149,000+ |
| **Languages** | English only | All languages |
| **Encoding** | Fixed (1 byte) | UTF-8, UTF-16, UTF-32 |
| **Web Standard** | Legacy | UTF-8 (dominant) |
| **Compatibility** | Limited | UTF-8 includes ASCII |
| **File Size** | Smaller (English) | Larger (multi-language) |

## Character Encoding Examples

### String Encoding

**"Hello" in ASCII:**
```
H     e     l     l     o
72    101   108   108   111
0x48  0x65  0x6C  0x6C  0x6F
```

**"Hello" in UTF-8 (same as ASCII):**
```
H     e     l     l     o
0x48  0x65  0x6C  0x6C  0x6F
```

**"你好" (Chinese "Hello") in UTF-8:**
```
你                          好
U+4F60                      U+597D
E4 BD A0                    E5 A5 BD
11100100 10111101 10100000  11100101 10100101 10111101
```

## Learning Objectives

By the end of this chapter, you should be able to:
- Understand ASCII encoding and its character ranges
- Convert characters to ASCII codes and vice versa
- Recognize ASCII patterns (case conversion, digit extraction)
- Understand Unicode and its purpose
- Compare UTF-8, UTF-16, and UTF-32 encodings
- Explain the relationship between ASCII and Unicode
- Work with character encoding in programming

## Python Example

Run the interactive example:

```bash
python ch11_coding_schemas.py
```

### What the Example Demonstrates

1. **ASCII Encoding:** Character to code conversion
2. **ASCII Table:** Display of character ranges
3. **Case Conversion:** Uppercase/lowercase manipulation
4. **String Encoding:** Converting text to byte sequences
5. **Unicode Code Points:** Beyond ASCII characters
6. **UTF-8 Encoding:** Variable-length encoding
7. **International Characters:** Multi-byte representations
8. **Emojis:** Modern Unicode support

### Sample Output

```
============================================================
CHAPTER 11: Coding Schemas (ASCII and Unicode)
============================================================

--- Example 1: ASCII Character Encoding ---
Character 'A':
  ASCII value: 65
  Hexadecimal: 0x41
  Binary:      01000001

Character 'a':
  ASCII value: 97
  Hexadecimal: 0x61
  Binary:      01100001

Difference: 32 (bit 5 flipped)
...
```

## Real-World Applications

### Text Processing
- **Text Editors:** Character display and manipulation
- **Word Processors:** Document encoding
- **Search Engines:** Text indexing and matching
- **Regular Expressions:** Pattern matching

### Data Transmission
- **Email:** SMTP uses 7-bit ASCII
- **HTTP:** Headers in ASCII, body in various encodings
- **JSON/XML:** UTF-8 for data interchange
- **Network Protocols:** Command strings in ASCII

### Programming
- **Source Code:** Usually UTF-8
- **String Literals:** Character sequences
- **Character Arrays:** Text buffers
- **I/O Operations:** Reading/writing text files

### Internationalization (i18n)
- **Websites:** UTF-8 for multilingual content
- **Applications:** Unicode for global users
- **Databases:** UTF-8/UTF-16 storage
- **Operating Systems:** Unicode for file names and UI

## Common Questions

**Q: Why is 'A' = 65 and 'a' = 97?**  
A: ASCII was designed so uppercase and lowercase differ by 32 (bit 5), making case conversion a simple bit operation.

**Q: Can I use ASCII for Chinese or Arabic?**  
A: No. ASCII only covers English. Use Unicode (UTF-8) for international characters.

**Q: Why is UTF-8 so popular?**  
A: It's backward compatible with ASCII, space-efficient for English text, and supports all Unicode characters.

**Q: What's the difference between UTF-8 and Unicode?**  
A: Unicode is the character set (defines code points). UTF-8 is an encoding (how to store those code points as bytes).

**Q: Why does "café" sometimes display as "café"?**  
A: Encoding mismatch! The file is UTF-8 but interpreted as Latin-1 (or vice versa).

## Best Practices

### ✅ DO
- Use UTF-8 for new projects
- Declare encoding in HTML/XML (`<meta charset="UTF-8">`)
- Handle encoding/decoding explicitly in code
- Test with non-ASCII characters
- Use Unicode-aware string functions

### ❌ DON'T
- Assume ASCII is sufficient for all text
- Mix encodings within a project
- Use extended ASCII (use UTF-8 instead)
- Ignore encoding errors in file I/O
- Hard-code character values (use named constants)

## Programming Examples

### Python
```python
# Character to code
ord('A')  # 65
ord('中') # 20013

# Code to character
chr(65)    # 'A'
chr(20013) # '中'

# String encoding
'Hello'.encode('utf-8')        # b'Hello'
'你好'.encode('utf-8')         # b'\xe4\xbd\xa0\xe5\xa5\xbd'

# String decoding
b'Hello'.decode('utf-8')       # 'Hello'
```

### C/C++
```c
char c = 'A';  // 65
printf("%c = %d (0x%02X)\n", c, c, c);
// Output: A = 65 (0x41)

// Case conversion
char upper = 'A';
char lower = upper + 32;  // 'a'
// OR
char lower = upper | 0x20;  // Set bit 5
```

## Key Takeaways

- ASCII: 7-bit (128 chars) standard for English text
- Unicode: Universal standard for all languages and symbols
- 🔤 UTF-8: Variable-length, ASCII-compatible, web standard
- 'A'=65, 'a'=97 (differ by 32, bit 5)
- 🔡 '0'=48, subtract 48 to get numeric value
- UTF-8 is the dominant encoding on the web
- Extended ASCII (128-255) is non-standard and problematic
- Always declare encoding explicitly in files and protocols

## Practice Exercises

1. What is the ASCII code for '5'? For 'M'?
2. Convert "Hello" to ASCII codes (decimal and hex)
3. Convert 01001000 01001001 to text
4. How do you convert 'B' to 'b' using bit operations?
5. Why can't ASCII represent "こんにちは" (Japanese "hello")?
6. What is the UTF-8 byte sequence for 'é' (U+00E9)?
7. Calculate: 'Z' - 'A' = ?
8. If a file shows garbage for "naïve", what's likely wrong?
9. How many bytes does "😀🎉" take in UTF-8?
10. Write code to check if a character is uppercase (using ASCII properties)

## Further Study

- Learn about character normalization (NFC, NFD)
- Study Unicode bidirectional algorithm (for Arabic, Hebrew)
- Explore emoji encoding and variants
- Investigate Base64 encoding
- Learn about URL encoding (percent-encoding)

---
<!-- License moved to dedicated LICENSE file -->
