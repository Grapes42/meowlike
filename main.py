#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

def main() -> None:
    screen_width = 30
    screen_height = 30

    map_width = 30
    map_height = 30

    tileset = tcod.tileset.load_tilesheet(
        "spritesheet.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@")
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "f")
    toeLicker = Entity(int(screen_width / 2 + 5), int(screen_height / 2), "T")
    potion = Entity(int(screen_width / 2 - 5), int(screen_height / 2 + 5), "!")
    potion = Entity(int(screen_width / 2 - 5), int(screen_height / 2 + 5), "!")
    entities = {npc, toeLicker, potion, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Meowlike",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()