import os
import subprocess
import shutil
from manim import *

# ===================  CONFIGURATION  ===================
cur_dir = os.path.dirname(os.path.realpath(__file__))
workspace = os.getcwd()
TEXT_FILE = os.path.join(cur_dir, "sentences.txt")    # File containing text sentences
TIMESTAMP_FILE = os.path.join(cur_dir, "timestamps.txt")  # Timestamps for each sentence
WHITEBOARD_VIDEO = os.path.join(cur_dir, "whiteboard.mp4")
OUTPUT_VIDEO = os.path.join(cur_dir, "final_output.mp4")
MANIM_OUTPUT_DIR = os.path.join(workspace, "media/videos")  # Manim saves videos here
FINAL_OUTPUT_DIR = os.path.join(workspace, "final_videos")  # Final output directory for processed videos
os.makedirs(FINAL_OUTPUT_DIR, exist_ok=True)
# =======================================================

class TextAnimationGenerator:
    """Generates Manim animations for each sentence in a text file."""

    def __init__(self, text_file):
        self.text_file = text_file
        self.sentences = self.read_sentences()

    def read_sentences(self):
        """Reads the sentences from the input text file."""
        with open(self.text_file, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]

    def generate_animations(self):
        """Generates Manim animations for all sentences."""
        for i, sentence in enumerate(self.sentences):
            # Create a custom Manim Scene for each sentence
            class SentenceScene(Scene):
                def construct(self):
                    text = Text(sentence).scale(0.8)
                    self.play(Write(text))
                    self.wait(2)

            # Render the scene for each sentence with a unique name
            scene = SentenceScene()
            scene.render()  # Render the scene

            # Define the generated file path and the new file name
            generated_file = os.path.join(MANIM_OUTPUT_DIR, "1080p60", "SentenceScene.mp4")
            output_filename = f"sentence_{i + 1}.mp4"  # Unique name for each sentence animation
            final_output_path = os.path.join(FINAL_OUTPUT_DIR, output_filename)

            # Move and rename the generated file
            if os.path.exists(generated_file):
                shutil.move(generated_file, final_output_path)
                print(f"Moved {output_filename} to {FINAL_OUTPUT_DIR}")
            else:
                print(f"Error: {generated_file} does not exist.")


# ===================  MAIN EXECUTION  ===================
if __name__ == "__main__":
    # Step 1: Generate text animations
    generator = TextAnimationGenerator(TEXT_FILE)
    generator.generate_animations()