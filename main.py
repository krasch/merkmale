from pathlib import Path

from pydantic import BaseModel
from pydantic_ai import Agent, BinaryContent

SYSTEM_PROMPT = "You are an expert ornithologist. You help users identify birds by identifying their features."


class Colors(BaseModel):
    white: bool
    light_brown_or_cream: bool
    grey: bool
    dark_or_medium_brown: bool
    black: bool
    yellow: bool
    orange: bool
    red: bool
    pink: bool
    blue: bool
    green: bool


class Sizes(BaseModel):
    roughly_swan_size: bool
    roughly_goose_size: bool
    roughly_duck_size: bool
    roughly_dove_size: bool
    roughly_sparrow_size: bool


class Shapes(BaseModel):
    short: bool
    hook: bool
    broad_and_cone_shaped: bool
    straight: bool
    flat: bool
    bent_downwards: bool
    long: bool

class BirdFeatures(BaseModel):
    plumage_colors: Colors
    size: Sizes
    beak_colors: Colors
    beak_shapes: Shapes
    leg_colors: Colors

    def pretty_print(self):
        bools_to_list = lambda bools: str([key for key in bools.__dict__.keys() if bools.__dict__[key]])  # ewww
        print(f"Plumage colors: {bools_to_list(self.plumage_colors)}")
        print(f"Size: {bools_to_list(self.size)}")
        print(f"Beak colors: {bools_to_list(self.beak_colors)}")
        print(f"Beak shapes: {bools_to_list(self.beak_shapes)}")
        print(f"Leg colors: {bools_to_list(self.leg_colors)}")


def infer(image: Path):
    assert image.exists()
    assert image.suffix in [".jpg", ".jpeg"]

    image_data = BinaryContent(data=image.read_bytes(), media_type='image/jpg')

    model = Agent("openai:gpt-5.6-luna", system_prompt=SYSTEM_PROMPT, output_type=BirdFeatures)
    result = model.run_sync([image_data])

    # print(result.output)
    result.output.pretty_print()


test_image = Path("bird.jpg")
infer(test_image)
