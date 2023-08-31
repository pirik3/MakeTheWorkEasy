words2paste := ["ep3", "ep2", "ep1", "r3ss", "r2ss", "r1ss", "r3ps", "r2ps", "r1ps", "tss", "tps", "dr1", "dr2"]

Shift::
MouseClickDrag, L, 558, 551, 1657, 425
Send {F2}
if (index + 1 > words2paste.count() || index == "") {
    index := 0
}
index++
clipboard := words2paste[index]
Send, ^v 
Send {Enter}
MouseMove, -359, 473
Sleep, 500
MouseClick, Left
return


Home::Pause
Esc::ExitApp
GuiClose:
ExitApp