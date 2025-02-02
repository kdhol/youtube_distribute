import os
import shutil

# install the library using pip install manim
from manim import *  # noqa: F403

# ===================  CONFIGURATION  ===================
cur_dir = os.path.dirname(os.path.realpath(__file__))
workspace = os.getcwd()
TEXT_FILE = os.path.join(cur_dir, "sentences.txt")  # File containing text sentences
OUTPUT_VIDEO = os.path.join(cur_dir, "final_output.mp4")
MANIM_OUTPUT_DIR = os.path.join(workspace, "media/videos")  # Manim saves videos here
FINAL_OUTPUT_DIR = os.path.join(
    workspace, "final_videos"
)  # Final output directory for processed videos
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
                # Set the frame rate and resolution globally
                config.pixel_height = (  # noqa: F405
                    700  # Adjust based on your desired resolution  # noqa: F405
                )
                config.pixel_width = 1200  # noqa: F405
                config.frame_height = 6  # Scene height  # noqa: F405
                config.frame_width = 12  # Scene width  # noqa: F405
                config.fps = 24  # Frame rate (adjust if needed)  # noqa: F405

                def construct(self):
                    text = Text(sentence).scale(0.8)
                    # Change the color of the text
                    text.set_color(WHITE)  # Change to your desired color

                    # TODO: uncomment this if you want to position the text at the bottom of the screen
                    # Position the text at the bottom of the screen
                    # text.shift(
                    #     DOWN * 3
                    # )  # Shift the text down (adjust the multiplier as needed)

                    self.play(Write(text))
                    # self.wait(1) # TODO: uncomment this of you need to show animation for longer

            # Render the scene for each sentence
            scene = SentenceScene()

            # Render the video
            scene.render()

            # Define the generated file path and the new file name
            manim_generated_file = os.path.join(
                MANIM_OUTPUT_DIR, "700p60", "SentenceScene.mp4"
            )
            output_filename = (
                f"sentence_{i + 1}.mp4"  # Unique name for each sentence animation
            )
            final_output_path = os.path.join(FINAL_OUTPUT_DIR, output_filename)

            # Move and rename the generated file
            if os.path.exists(manim_generated_file):
                shutil.move(manim_generated_file, final_output_path)
                print(f"Moved {output_filename} to {FINAL_OUTPUT_DIR}")
            else:
                print(f"Error: {manim_generated_file} does not exist.")


# ===================  MAIN EXECUTION  ===================
if __name__ == "__main__":
    # Step 1: Generate text animations
    generator = TextAnimationGenerator(TEXT_FILE)
    generator.generate_animations()

    # # Step 2: Overlay animations on whiteboard video
    # overlay = VideoOverlay(WHITEBOARD_VIDEO, TIMESTAMP_FILE, OUTPUT_VIDEO)
    # overlay.overlay_text_animations()
