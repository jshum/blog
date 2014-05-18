# Zanhealth
---
1. ### [Work Orders](#one)
	*  [A. Work Order List](#1.A)
	*  [B. Work Order Overview](#1.B)
	<!--
		*  [C. Details](#1.C)
		*  [D. Comments](#1.D)
		*  [E. Cost](#1.E)
		*  [F. Labor Hours](#1.F)
	-->
2. ### [Preventative Maintenance](#two)
	*  [Preventative Maintenance Details](#2.B)
3. ### [Work Requests](#three)
4. ### [Dashboard](#four)
	<!--
	*  [A. Statuses](#4.1)
	*  [B. Finances](#4.2)
	*  [C. Labor Hours](#4.3)
	-->
5. ### [Data Input/Output](#five)
6. ### [Managing Views](#six)
	* [A. Search, Filter, and Sort](#6.A)
	* [B. Archive](#6.B)
7. ### [Language](#seven)
---

## <a id = "one"></a> Work Orders
The work order is the basic unit of Zanhealth's function. The work order page is where users can see what repairs need to be made, along with all relevant information for the item and repair. To add a work order, click the "+" button in the upper right corner.

![Overview](work_orders.png)

###<a id = "1.A"></a> A. Work Order List

This is a list containing basic information on each work order. By default, work orders are sorted by date, with the soonest date appearing earliest. [(Sort work orders.)](#6.A) Clicking on a work order will open [a more detailed view.](#1.B)

The color tag on the left side indicates status.

* <font color = "#006300"> Green = completed </font>
* <font color = "FFCC00"> Yellow = started </font>
* <font color = "red"> Red = not started/expired </font>

###<a id = "1.B"></a> B. Work Order Overview

Each work order has lots of useful information associated with it. The status, owner, department, expiration date, and description can be toggled upon clicking. The most useful of these will most likely be the status, which can change between "Started", "Unstarted", and "Completed." Saving changes will cause the status in the overview list (i.e. color) to automatically update. 

![Changing work request status](changing_work_request_status.png "Changing work request status")

*Example: changing work request status.*

#### The interfaces of (C), (D), (E), and (F) allow the user to view and edit even more detailed information:

####<a id = "1.C"></a> C. Details

By clicking ![details icon](details_icon.png), a user can view the details on cause, action, and prevention. These can be easily updated by editing and hitting "Save changes".

![Details](details.png)

*Example: Editing action taken.*


####<a id = "1.D"></a> D. Comments 

Clicking ![comments icon](comments_icon.png) will bring up a log of technician comments. New comments can be added by typing in the bottom text box and hitting the ">" button (highlighted in red).

![Comments](comments.png)

*Example: Adding comment 3 to comments 1 and 2.*
####<a id = "1.E"></a> E. Cost 

The cost view can be accessed by clicking ![cost icon](cost_icon.png). You can view and update the cost of a repair by adding the necessary items. 

![Cost](cost.png)

*Example: Adding the cost of screws to the cost of this repair.*

####<a id = "1.F"></a> F. Labor Hours 

The total number of hours a repair has been worked on, broken down by technician, can be accessed by clicking ![LH_icon](LH_icon.png). The individual technician, date, and number of hours worked can be edited and saved.

![Labor Hours](labor_hours.png)

*Example: Adding UserAHE2's 5 hours to the total time of this repair.*

---

## <a id = "two"></a> Preventative Maintenance
Preventative maintenance refers to regularly scheduled maintenance routines that recur at set intervals. The list on the left works in a similar way to the [work order list](#1.A). The preventative maintenance list is sorted by due date, with the maintenance routine with the soonest due date appearing first.

### <a id = "2.B"></a> Preventative Maintenance Request Details

Clicking on a specific maintenance request will bring up the following interface:

![Preventative Maintenance](preventative_maintenace.png)

###A. Action Bar

Convert and hide are the most important actions for a work request.

**Convert** converts this preventative maintenance request into a work request, thereby putting it into the work pipeline. That is, if a maintenance request is not converted, it will remain in the preventative maintenance list, but will not show up as a work request. Pressing convert brings up a dialog that prompts the user for information: "Cause Description" must be filled out.

**Hide** [archives](#6.B) this preventative maintenance request.

###B. Set recur time

Toggle the prompts to set how often you want the preventative maintenance request to recur.

---

## <a id = "three"></a> Work Requests

A work request is the precursor to a work order. Work requests must be approved before they are cleared to become work orders. The interface for work requests works almost exactly the same way as [preventative maintenance](#two); again, this can be done with **Convert to Work Order**. 

Work requests can be sorted by either requester or department (both in alphabetical order).


## <a id = "four"></a> Dashboard
The **Dashboard** provides analytics on three crucial logistical areas:

### <a id = "4.1"></a> Statuses

Make chartz

### <a id = "4.2"></a> Finances

More chartz

### <a id = "4.3"></a> Labor Hours

Chartz on chartz on chartz

---

## <a id = "five"></a> Data Input/Output

Data input and output is managed by the gray bar the top of the screen.

![data bar](data_bar.png)

####Data Input

The ![plus](plus.png) icon allows a user to create a single instance of the current view (work order, preventative maintenance, or work request).

Soon to come will be an **Import Data* button that allows the user to upload an <code>.csv</code> spreadsheet of equipment.

####Data Output

The **Print** icon allows the user to print a data spreadsheet of the current view. 

The **Export Data** icon offers the same functionality as **Print**, but allows the user to download a <code>.csv</code> version of the spreadsheet. 

---

## <a id = "six"></a> Managing Views

Views can be managed by the gray bar at the top of the screen. 

![views bar](views_bar.png)

### <a id = "6.A"></a> Search, Filter, and Sort 

**Filter** only displays the work requests that fit certain criteria: it can be used to filter work orders by status. **Filter** is unique to the work request menu.

**Sort** orders the work requests by one of the following criteria:

* Date Created
* Date Started
* Requester
* Owner 
* Status

**Search** returns the work requests that have a match with the query string.

### <a id = "6.B"></a> Archive

Orders and requests in Zanhealth are either **visible** or **hidden**. A hidden request/order is archived; it is either irrelevant, denied, or completed.

A **work order** can be archived by clicking on the archive icon.

![archive icon](archive_view.png)

**Preventative maintenance requests** and **work requests** can be archived by clicking the hide button in the detailed dialog box.

![hide](hide.png)

An archived item can be **unarchived** by performing the same action as hiding. In the case of requests, "unhide" will take the place of "hide".

![unhide](unhide.png)

---

## <a id = "seven"></a> Language

Language can be toggled by using the buttons under **Dashboard**. Currently available languages include English, Swahili, and Creole.

---
