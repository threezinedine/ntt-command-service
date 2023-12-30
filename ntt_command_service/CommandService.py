from typing import *
from .ICommand import ICommand
from .ICommandService import ICommandService
from .Exceptions import *
from ntt_signal import *


class CommandService(Signal, ICommandService):
    def __init__(self) -> None:
        super().__init__()

        self._iCommands: List[ICommand] = []

    def AddCommand(self, iCommand: ICommand) -> None:
        if iCommand.CanExecute():
            iCommand.Execute()
            self._iCommands.append(iCommand)
            self.Emit()

    def Undo(self) -> None:
        if self.CanUndo():
            self._iCommands[-1].Undo()
            self._iCommands.pop()
            self.Emit()
        else:
            raise CommandServiceEmptyError("Command Service has no command")

    def CanUndo(self) -> bool:
        return len(self._iCommands) != 0

    def Clear(self) -> None:
        bCanUndo = self.CanUndo()
        self._iCommands = []
        if bCanUndo:
            self.Emit()

    def Test(self) -> None:
        pass
