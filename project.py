# Copyright 2020, Brigham Young University-Idaho. All rights reserved.
import tkinter as tk
from geopy.geocoders import Nominatim
from geopy import distance

geolocator = Nominatim(user_agent="geoapiexercise")


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Rida App")
    frm_main.pack(padx=200, pady=100, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and each
# widget is an object, the code to make a GUI usually has many variables
# to store the many objects. Because there are so many variable names,
# programmers often adopt a naming convention to help a programmer keep
# track of all the variables. One popular naming convention is to type a
# three letter prefix in front of the names of all variables that store
# GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # create a label that displays the app name
    lbl_app = tk.Label(frm_main, text="Rida App", width=10, font=("bold", 20), fg="red")
    

    # Create a label that displays "current location:"
    lbl_location = tk.Label(frm_main, text="Current location:", font=("bold", 10))

    # Create a integer entry box where the user will enter her location.
    ent_location = tk.Entry(frm_main, width=75, font=("bold", 10))

    # Create a label that displays "Destination:"
    lbl_destination = tk.Label(frm_main, text="Destination:", font=("bold", 10))

    # Create a integer entry box where the user will enter her destination.
    ent_destination = tk.Entry(frm_main, width=75, font=("bold", 10))

    # Create a label that displays "Base price:"
    lbl_base = tk.Label(frm_main, text="Base price:", font=("bold", 11))

    # Create labels that will display the results.
    output_base = tk.Label(frm_main, width=20, font=("bold", 11))

     # Create a label that displays "Premium price:"
    lbl_premium = tk.Label(frm_main, text="Premium price:", font=("bold", 11))

    # Create labels that will display the results.
    output_premium = tk.Label(frm_main, width=20, font=("bold", 11))

    # create a label that displays "Geolocator"
    lbl_locator = tk.Label(frm_main, text="Geolocator:", font=("bold", 11))

    # Create labels that will display the results.
    output_locator = tk.Label(frm_main, width=50, font=("bold", 11))


    # Create the Confirm button.
    btn_confirm = tk.Button(frm_main, text="Check price", bg="green", fg="white", borderwidth=5, font=("bold", 11))

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear", bg="red", fg="white", borderwidth=5, font=("bold", 11))

    # Layout all the labels, entry boxes, and buttons in a grid.
    # title
    lbl_app.grid(row=0, column=1)


    # inputs
    lbl_location.grid(row=1, column=0, padx=10, pady=10)
    ent_location.grid(row=2, column=1, padx=10, pady=10)
    
    lbl_destination.grid(row=3, column=0, padx=10, pady=10)
    ent_destination.grid(row=4, column=1, padx=10, pady=10)
    
    # control
    btn_confirm.grid(row=6, column=2, padx=3, pady=3, columnspan=5, sticky="W")
    btn_clear.grid(row=6, column=7, padx=3, pady=3, columnspan=5, sticky="W")

    # outputs
    lbl_locator.grid(row=8, column=0, padx=(30,3), pady=3)
    output_locator.grid( row=9, column=1, padx=3, pady=3)

    lbl_base.grid(row=10, column=1, padx=(30,3), pady=3)
    output_base.grid( row=11, column=1, padx=3, pady=3)

    lbl_premium.grid(row=12, column=1, padx=(30,3), pady=3)
    output_premium.grid( row=13, column=1, padx=3, pady=3)


    # another way to style the widgets but still trying to understand it to use it effectively
    # title
    

    # # inputs
    # lbl_location.place(x=150, y =100)
    #  ent_location.place(x=200, y=130)
   

    # lbl_destination.place(x=150, y=160)
    # ent_destination.place(x=200, y=190)
    
    # # control
    # btn_confirm.place(x=600, y=230)
    # btn_clear.place(x=710, y=230)

    # # outputs
    # lbl_locator.place(x=150, y=300)
    # output_locator.place(x=190, y=330)

    # lbl_base.place(x=150, y=370)
    # output_base.place(x=190, y=400)

    # lbl_premium.place(x=150, y=440)
    # output_premium.place(x=190, y=470)
    
    

    # This function will be called each time the user clicks on confirm button.
    def confirm():
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """

        
        try:
            # Get the user location .
            location = ent_location.get()

            # get the user's destination

            destination = ent_destination.get()

            # use the imported library to search for the distance in Km 
            # between the location and destination
            # and use the result to calculate the base and premium prices

            place1 =geolocator.geocode(location)
            place2=geolocator.geocode(destination)

            # print(place1)
            # print(place2)

            loc1_lat, loc1_lon =(place1.latitude), (place1.longitude)

            loc2_lat, loc2_lon =(place2.latitude), (place2.longitude)

            locate1 = (loc1_lat, loc1_lon)
            locate2 = (loc2_lat, loc2_lon)

            

            actual_distance = (distance.distance(locate1, locate2).km, "kms")

            initial = float(actual_distance[0])

            # call the calculate and calculate1 functions to get the base price and premium price

            final_baseprice = calculate(initial)
            final_premiumprice = calculate1(initial)            

            
            

            # for the output, display the destination in km, and the base price
            # and premium prices for the user to see.
             
            output_locator.config(text=f"The distance from {location} to {destination} is: {initial:.2f} kms")

            output_base.config(text=f"${final_baseprice:.1f}", fg="red")

            output_premium.config(text=f"${final_premiumprice:.1f}", fg="red")

            


            
        except:
            # When the user enters a wrong location or destination 
            output_locator.config(text=f"Incorrect location or destination; please check your spelling.")
            output_base.config(text="")
            output_premium.config(text="")
            
        


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_location.delete(0, tk.END)
        ent_destination.delete(0, tk.END)
        output_base.config(text="")
        output_premium.config(text="")
        output_locator.config(text="")
    
        ent_location.focus()
        ent_destination.focus()


    # Bind the confirm function to the confirm button so that
    # the confirm function will be called when the user clicks
    # the confirm button
    btn_confirm.config(command=confirm)


    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the location and destinantion.
    ent_location.focus()
    ent_destination.focus()



def calculate(distance):
    base = distance/10      
    return base
        
def calculate1(distance):
    premium = distance/5
    return premium
    

# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
