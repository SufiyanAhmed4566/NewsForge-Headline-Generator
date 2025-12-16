# NewsForge: Headline Generator

A Python-based Fake News Headline Generator that creates humorous and creative headlines using the Factory Design Pattern. Perfect for demonstrating Python programming skills and Object-Oriented Programming concepts.

## Features

- Factory Design Pattern Implementation: Clean separation of headline creation logic
- Four Categories: Tech, Sports, Funny, and Mystery headlines
- Random Generation: Generate random headlines or choose specific categories
- History Tracking: Keep track of all generated headlines
- Simple CLI Interface: User-friendly command-line interface
- No External Dependencies: Pure Python - no additional libraries required

## Quick Start

1. Clone the repository:
```
git clone https://github.com/yourusername/newsforge-headline-generator.git
cd newsforge-headline-generator
```

2. Run the program:
```
python newsforge.py
```

3. Choose from the menu:
   - Generate random headlines
   - Generate category-specific headlines
   - View generation history
   - Exit the program

## Project Structure

newsforge.py
- HeadlineFactory Class (Factory Pattern)
  - tech_words dictionary
  - sports_words dictionary
  - funny_words dictionary
  - mystery_words dictionary

- NewsForgeApp Class
  - Menu system
  - History tracking
  - User interaction

- Main execution flow

## Design Pattern: Factory Method

The project implements the Factory Design Pattern where:
- HeadlineFactory class acts as the factory
- create_headline() method is the factory method
- Different headline types are created based on categories
- Clean separation between creation logic and usage

## Code Highlights

```
# Factory Pattern Implementation
class HeadlineFactory:
    def create_headline(self, category='random'):
        # Factory method that creates different headline types
        # based on the category parameter
        pass

# Object-Oriented Programming
class NewsForgeApp:
    def __init__(self):
        self.factory = HeadlineFactory()  # Composition
        self.history = []  # Encapsulation
```

## Sample Output

```
==================================================
         NEWSFORGE HEADLINE GENERATOR
==================================================

MAIN MENU:
1. Generate Random Headline
2. Generate Tech Headline
3. Generate Sports Headline
4. Generate Funny Headline
5. Generate Mystery Headline
6. Show Generation History
7. Exit
------------------------------

Enter your choice (1-7): 1

CREATING HEADLINE...

CATEGORY: FUNNY
HEADLINE: LOL: Pizza declared war on vegetables!
```

## Technologies Used

- Python 3.x
- Object-Oriented Programming
- Factory Design Pattern
- CLI Development

## Python Concepts Demonstrated

- Object-Oriented Programming (OOP): Classes, objects, encapsulation
- Design Patterns: Factory Method Pattern
- Data Structures: Lists, dictionaries, tuples
- Control Flow: Loops, conditionals, functions
- String Manipulation: Formatting, concatenation
- Error Handling: Try-except blocks
- Modular Programming: Separated concerns

## Contributing

Contributions are welcome! Feel free to:
- Add more headline categories
- Implement additional design patterns
- Improve the user interface
- Add more word options

## License

This project is open source and available under the MIT License.

Star this repo if you find it useful!
