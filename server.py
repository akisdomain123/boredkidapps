from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # This allows requests from the frontend

# Fun activity ideas for kids
activities = [
    "Build a fort with pillows and blankets!",
    "Create a treasure hunt with hidden clues.",
    "Draw a comic strip about a superhero you invent.",
    "Make a DIY volcano with baking soda and vinegar.",
    "Try a new science experiment with household items.",
    "Make homemade slime or playdough.",
    "Create your own board game and play it with family.",
    "Build a tower using only paper and tape!",
    "Write a short story and illustrate it.",
    "Make a nature collage using leaves and flowers.",
    "Do 10 jumping jacks and run around like a superhero!",
    "Try a kid-friendly yoga or dance workout.",
    "Make shadow puppets with a flashlight.",
    "Try to balance a spoon on your nose!",
    "Bake cookies and decorate them with colorful icing.",
    "Write a letter to your future self.",
    "Learn to say hello in five new languages.",
    "Make a time capsule to open in a year.",
    "Create a funny skit and perform it for family.",
    "Try a no-screen day challenge for fun!"
]

@app.route('/idea', methods=['GET'])
def get_idea():
    return jsonify({'idea': random.choice(activities)})

if __name__ == '__main__':
    app.run(debug=True)

