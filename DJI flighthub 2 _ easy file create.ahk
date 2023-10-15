words2paste := ["SS", "PS", "LE", "TE"]
words2paste2 := ["Blade A", "Blade B", "Blade C"]

Shift::
MouseClick, Left
MouseGetPos, outx, outy
if (index + 1 > words2paste.count() || index == "") {
    index := 0
}
index++
clipboard := words2paste[index]
Send, ^v 
MouseMove, 1128, 625
Sleep, 500
MouseClick, Left
MouseMove, %outx%, %outy%
return

Tab::
MouseClick, Left
MouseGetPos, outx, outy
if (index + 1 > words2paste2.count() || index == "") {
    index := 0
}
index++
clipboard := words2paste2[index]
Send, ^v 
MouseMove, 1128, 625
Sleep, 500
MouseClick, Left
MouseMove, %outx%, %outy%
return


Home::Reload
Esc::ExitApp
GuiClose:
ExitApp
