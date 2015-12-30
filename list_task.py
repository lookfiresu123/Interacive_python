# Application: list tasks

# import module
import simpleguitk as simplegui

# define globals
tasks = []
frame_width = 600
frame_height = 400
font_color = "White"
font_size = 20
initial_position = [font_size, font_size]

# define helper functions which consist of event handlers

# define event handlers
# handler for add a new task
def new(task):
	tasks.append(task)

# handler for remove a task by tasknum
def remove_num(tasknum):
	n = int(tasknum)
	if n > 0 and n <= len(tasks):
		tasks.pop(n - 1)

# handler for remove a task by taskname
def remove_name(taskname):
	if taskname in tasks:
		tasks.remove(taskname)		# or "tasks.pop(tasks.index(taskname))"

# handler for clear all the task in tasks list
def clear():
	del tasks[:]

def draw(canvas):
	# if current_position = initial_position, then change the current_position will also change initial_position, because it's a reference relative
	# so use current_position = list(initial_position), then they are copy relative
	current_position = list(initial_position)
	# print initial_position
	for i in tasks:
		current_position[1] += font_size
		string_name = str(tasks.index(i) + 1) + ": " + i
		canvas.draw_text(string_name, current_position, font_size, font_color)

# create frame
frame = simplegui.create_frame("List Tasks", frame_width, frame_height)

# register event handlers into frame
frame.add_input("New task:", new, 200)
frame.add_input("Remove task number:", remove_num, 200)
frame.add_input("Remove task:", remove_name, 200)
frame.add_button("Clear All:", clear, 50)
frame.set_draw_handler(draw)

# start frame
frame.start()
