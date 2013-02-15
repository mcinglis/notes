# Windows and buffers

> A buffer is the in-memory text of a file.
> A window is a viewport on a buffer.
> A tab page is a collection of windows.

A buffer is considered *active* if it is displayed in a window, and *hidden* if it is not displayed.

## Opening windows

* `C-w s` and `:sp` create a duplicate window below the current window
* `C-w v` and `:vs` create a duplicate window to the right of the current window
* `C-w n` and `:new` create a window with a fresh buffer below the current window
* `:vnew` creates a window with a fresh buffer to the right of the current window

## Closing windows

* `C-w q` and `:q[uit]` quit the current window
* `C-w c` and `:clo[se]` close the current window; it is equivalent to `C-W q` when `hidden` isn't set

## Navigating windows

* `C-w w` cycles between the open windows
* `C-w h`, `C-w j`, `C-w k`, `C-w l` moves the focus around windows

## Resizing windows

* `C-w <n>+` increase the height of the current window by n lines
* `C-w <n>-` decrease the height of the current window by n lines
* `C-w _` maximizes the height of the current window
* `C-w |` maximizes the width of the current window

## Moving windows

* `C-w r` rotates all windows
* `C-w x` exchanges the current window with its neighbor
* `C-w H`, `C-w J`, `C-w K`, `C-w L` move the current window to the far direction

