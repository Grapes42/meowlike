from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        """
        Arrow key movement:
               up
               |
        left — z — right
               |
              down

        """
        if key == tcod.event.KeySym.UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.KeySym.DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.KeySym.LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.KeySym.RIGHT:
            action = MovementAction(dx=1, dy=0)

            """
        YUHJKLBN Movement:
         y  k  u
          \ | /
        h — z — l
          / | \
         b  j  n
            """
        elif key == tcod.event.KeySym.y:
            action = MovementAction(dx=-1, dy=-1)
        elif key == tcod.event.KeySym.k:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.KeySym.u:
            action = MovementAction(dx=+1, dy=-1)
        elif key == tcod.event.KeySym.h:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.KeySym.l:
            action = MovementAction(dx=+1, dy=0)
        elif key == tcod.event.KeySym.b:
            action = MovementAction(dx=-1, dy=+1)
        elif key == tcod.event.KeySym.j:
            action = MovementAction(dx=0, dy=+1)
        elif key == tcod.event.KeySym.n:
            action = MovementAction(dx=+1, dy=+1)

        # Quits program when esc is pressed 
        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action