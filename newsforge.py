"""
NEWSFORGE: Simple Headline Generator
A clean, single-pattern headline generator
"""

import random

# ============================================
# 1. FACTORY PATTERN IMPLEMENTATION
# ============================================

class HeadlineFactory:
    """
    Factory Pattern Implementation
    Creates different types of headlines based on categories
    """
    
    def __init__(self):
        # Initialize word banks for different categories
        self.tech_words = {
            'subjects': ['AI', 'Blockchain', 'Quantum Computer', 'VR Headset', 'Smartphone', 'Drone'],
            'actions': ['invented', 'hacked', 'revolutionized', 'transformed', 'disrupted'],
            'objects': ['the internet', 'social media', 'cryptocurrency', 'your privacy', 'smart homes']
        }
        
        self.sports_words = {
            'subjects': ['Football Team', 'Basketball Player', 'Tennis Star', 'Olympic Athlete', 'Coach'],
            'actions': ['won championship', 'broke record', 'signed contract', 'retired from', 'joined'],
            'objects': ['the game', 'major league', 'gold medal', 'hall of fame', 'rival team']
        }
        
        self.funny_words = {
            'subjects': ['Cat', 'Pizza', 'Sleeping Dog', 'Coffee', 'Monday Morning'],
            'actions': ['declared war on', 'invented new dance for', 'started podcast about', 'became CEO of'],
            'objects': ['homework', 'alarm clocks', 'vegetables', 'traffic', 'waking up early']
        }
        
        self.mystery_words = {
            'subjects': ['Secret Agent', 'Ancient Artifact', 'Ghost', 'Lost City', 'UFO'],
            'actions': ['disappeared from', 'found clue about', 'revealed truth behind', 'solved mystery of'],
            'objects': ['hidden treasure', 'time travel', 'parallel universe', 'conspiracy theory']
        }
    
    def create_headline(self, category='random'):
        """
        Factory method to create headlines
        """
        if category == 'random':
            categories = ['tech', 'sports', 'funny', 'mystery']
            category = random.choice(categories)
        
        # Get the appropriate word bank
        if category == 'tech':
            words = self.tech_words
            templates = [
                "BREAKING: {subject} {action} {object}!",
                "Tech Update: {subject} just {action} {object}",
                "Future is Here: {subject} {action} {object}"
            ]
        elif category == 'sports':
            words = self.sports_words
            templates = [
                "SPORTS ALERT: {subject} {action} {object}!",
                "Game Changer: {subject} {action} {object}",
                "Exclusive: {subject} {action} {object}"
            ]
        elif category == 'funny':
            words = self.funny_words
            templates = [
                "LOL: {subject} {action} {object}! 😂",
                "You Won't Believe: {subject} {action} {object}",
                "Wait, What? {subject} {action} {object}"
            ]
        elif category == 'mystery':
            words = self.mystery_words
            templates = [
                "MYSTERY SOLVED: {subject} {action} {object}!",
                "Breaking News: {subject} {action} {object}",
                "Shocking: {subject} {action} {object}"
            ]
        else:
            return "Invalid category"
        
        # Generate random words
        subject = random.choice(words['subjects'])
        action = random.choice(words['actions'])
        obj = random.choice(words['objects'])
        
        # Select random template
        template = random.choice(templates)
        
        # Create headline
        headline = template.format(subject=subject, action=action, object=obj)
        
        return headline, category

# ============================================
# 2. SIMPLE APPLICATION CLASS
# ============================================

class NewsForgeApp:
    """
    Simple application that uses the Factory Pattern
    """
    
    def __init__(self):
        self.factory = HeadlineFactory()
        self.history = []
    
    def display_banner(self):
        """Show application banner"""
        print("\n" + "=" * 50)
        print("         📰 NEWSFORGE HEADLINE GENERATOR 📰")
        print("=" * 50)
    
    def display_menu(self):
        """Show main menu"""
        print("\n📋 MAIN MENU:")
        print("1. 🎲 Generate Random Headline")
        print("2. 💻 Generate Tech Headline")
        print("3. ⚽ Generate Sports Headline")
        print("4. 😂 Generate Funny Headline")
        print("5. 🔍 Generate Mystery Headline")
        print("6. 📜 Show Generation History")
        print("7. 🚪 Exit")
        print("-" * 30)
    
    def generate_and_display(self, category='random'):
        """Generate and display a headline"""
        print("\n" + "✨" * 20)
        print("CREATING HEADLINE...")
        
        headline, cat = self.factory.create_headline(category)
        self.history.append((headline, cat))
        
        print(f"\n📰 CATEGORY: {cat.upper()}")
        print(f"📝 HEADLINE: {headline}")
        print("✨" * 20)
    
    def show_history(self):
        """Show previously generated headlines"""
        if not self.history:
            print("\nNo headlines generated yet!")
            return
        
        print("\n" + "📜" * 15)
        print("GENERATION HISTORY")
        print("📜" * 15)
        
        for i, (headline, category) in enumerate(self.history, 1):
            print(f"\n{i}. [{category.upper()}]")
            print(f"   {headline}")
        
        print(f"\nTotal headlines: {len(self.history)}")
    
    def run(self):
        """Run the main application"""
        self.display_banner()
        
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-7): ").strip()
                
                if choice == '1':
                    self.generate_and_display('random')
                elif choice == '2':
                    self.generate_and_display('tech')
                elif choice == '3':
                    self.generate_and_display('sports')
                elif choice == '4':
                    self.generate_and_display('funny')
                elif choice == '5':
                    self.generate_and_display('mystery')
                elif choice == '6':
                    self.show_history()
                elif choice == '7':
                    print("\nThank you for using NewsForge!")
                    print(f"Total headlines created: {len(self.history)}")
                    print("Goodbye! 👋")
                    break
                else:
                    print("Please enter a number between 1 and 7")
            
            except KeyboardInterrupt:
                print("\n\nProgram stopped. Goodbye!")
                break
            except Exception as e:
                print(f"\nAn error occurred: {e}")
                print("Please try again.")

# ============================================
# 3. MAIN EXECUTION
# ============================================

def main():
    """Main function to run the application"""
    print("Starting NewsForge Headline Generator...")
    app = NewsForgeApp()
    app.run()

# ============================================
# 4. SAMPLE HEADLINE GENERATOR (BONUS)
# ============================================

def quick_demo():
    """Quick demonstration of the generator"""
    print("\n" + "🚀" * 25)
    print("QUICK DEMO: Generating 5 random headlines")
    print("🚀" * 25)
    
    factory = HeadlineFactory()
    
    for i in range(1, 6):
        headline, category = factory.create_headline('random')
        print(f"\n{i}. [{category.upper()}]")
        print(f"   {headline}")
    
    print("\n" + "✅" * 25)
    print("Demo completed!")

# ============================================
# 5. PROGRAM ENTRY
# ============================================

if __name__ == "__main__":
    print("Welcome to NewsForge!")
    print("A simple headline generator using Factory Pattern")
    
    # Ask if user wants quick demo or full app
    while True:
        print("\nOptions:")
        print("1. Run Quick Demo (5 random headlines)")
        print("2. Run Full Application")
        print("3. Exit")
        
        option = input("\nChoose option (1-3): ").strip()
        
        if option == '1':
            quick_demo()
        elif option == '2':
            main()
            break
        elif option == '3':
            print("Goodbye! 👋")
            break
        else:
            print("Please choose 1, 2, or 3") 

