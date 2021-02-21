# Programming-in-Python
Write a script that draws the french flag. The strips are to be 100 wide and 200 tall which will give the flag the correct proportions.
Tip: The drawing itself does not need more than ten lines, however there needs to be a external loop to iterate over the three rectangles that the flag is composed of.
The standard Python distribution comes with a module called turtle that allows the user to draw a world and populate it with objects. One of the objects that can be drawn is, as the name of the module suggests, a turtle. The user can manipulate the objects in the world and move them around. The module is primarily for educational purposes but it can be used to draw graphs, curves and diagrams.

At the command prompt >>> (either in a terminal or in IDLE's command screen), write the following commands to start using the turtle module.
Import the turtle module:
>>> import turtle
Create a turtle:
>>> t = turtle.Turtle()
When the command is executed, a new window will open and a tiny figure will be placed in the middle. The window has a coordinate system with (0, 0) in the middle, where the x and y axis would meet.

The variable t in the code refers to a turtle object. The turtle has a set of methods that can be used to tell the turtle to do things. A method is a function that can only be used on an associated object, the turtle in this case. To call these methods you use dot notations. Compare this to the method append on list objects!

For example, this statement will make the turtle look more like a turtle:
>>> t.shape('turtle').

Run the following statements in order:

>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.circle(100)
Create a new python script file using the IDLE3 Python editor.

Copy and paste the code from the box to the right into your new file. The script will create a slightly more advanced figure.

Save the file and run it!

Try re-running the code with different values for the color (t.color()), length (t.forward()) and angle (t.left()).
The turtle object has a large set of methods. After you've imported the turtle module, you can use the following function to print all of the methods in the module.

>>> dir(turtle)

You can use the function help() to get information regarding a specific method in the module, i.e.

>>>help(turtle.forward)

The most important methods in the turtle module are can be found in the turtle graphics mini lesson. You can find the official turtle documentation here.

We will now illustrate concepts introduced in previous lessons using the turtle module, e.g. the if and while statements.

Tip: Use the -i flag when running your script, i.e.
python -i filename,
and the window will not close when the script has completed the execution.
