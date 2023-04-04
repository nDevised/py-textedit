Simple Python based text-editor. 
Inspired by "ed" text editor 

+------------------------------------------------------------------------------+
|                               Ed Text Editor                                 |
+------------------------------------------------------------------------------+
| Commands |  Action   |          Usage         |         Semantics           |
+------------------------------------------------------------------------------+
|    a     | Add text  | a                      | Add lines of text after the |
|          |           |                        | current line. End input with|
|          |           |                        | an empty line. Can add lines|
|          |           |                        | to an empty file.           |
+------------------------------------------------------------------------------+
|    d     | Delete    | d                      | Delete current line. An     |
|          |           | d n                    | error if the file is empty. |
|          |           | d -n                   |                             |
+------------------------------------------------------------------------------+
|    i     | Insert    | i                      | Insert lines of text before |
|          |           |                        | current line. End input with|
|          |           |                        | empty line. Can insert lines|
|          |           |                        | to an empty file.           |
+------------------------------------------------------------------------------+
|    l     | Load      | l fname                | Read file named "fname". An |
|          |           |                        | error if the open fails.    |
+------------------------------------------------------------------------------+
|    p     | Print     | p                      | Print current line. No error|
|          |           | p n                    | if file is empty.           |
|          |           | p -n                   |                             |
+------------------------------------------------------------------------------+
|    q     | Quit      | q                      | Exit the program. No check  |
|          |           |                        | if the user failed to write |
|          |           |                        | out previous file.          |
+------------------------------------------------------------------------------+
|    r     | Replace   | r text1 text2          | If "text1" is present in    |
|          |           | r text1                | current line, replace it    |
|          |           |                        | with "text2" (only once).   |
+------------------------------------------------------------------------------+
|    s     | Sort      | s                      | Sort the lines in the file  |
|          |           |                        | into ascending order.       |
+------------------------------------------------------------------------------+
|    w     | Write     | w fname                | Write to file "fname". An   |
|          |           | w                      | error if the open fails.    |
+------------------------------------------------------------------------------+
|    /     | Search    | / text1                | Search from next line for   |
|          | forward   |                        | "text1", wrapping around to |
|          |           |                        | file head if needed.        |
+------------------------------------------------------------------------------+
|    ?     | Search    | ? text1                | Search from previous line   |
|          | backward  |                        | for "text1", wrapping around|
|          |           |                        | to file tail if needed.     |
+------------------------------------------------------------------------------+
|   <n>    | Line      | <n>                    | Go to line <n>. It is an    |
|          | number    |                        | error to go beyond the end  |
|          |           |                        | of file or before the first |
|          |           |                        | line in the file.           |
+------------------------------------------------------------------------------+
|   <>     | Print     | <>                     | Print next line. No printing|
|          | next      |                        | if next line is end of file.|
+------------------------------------------------------------------------------+
