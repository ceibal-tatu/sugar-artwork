${
import math

def my_floor(num):
    return int(math.floor(num))

def my_ceil(num):
    return int(math.ceil(num))


# Should we set the line width in the engine to 2.25, and draw non pixel aligned lines?
# Are these already the correct sizes for the XO?

# These sizes need to be sanity checked ...
if scaling == "100":
    xo = True
    icon_base = 11
else: # About 72% of the XO size, adjusted so that eg. toolbuttons work
    xo = False
    icon_base = 8               # 7.92

}
${
icon_small = icon_base * 3
icon_large = icon_base * 5

small_icons = [ "gtk-menu", "gtk-dnd", "gtk-small-toolbar", "gtk-button" ]
large_icons = [ "gtk-large-toolbar" ]

icon_sizes = []
for icon in small_icons:
    icon_sizes += [icon + "=" + str(icon_small) + ',' + str(icon_small)]
for icon in large_icons:
    icon_sizes += [icon + "=" + str(icon_large) + ',' + str(icon_large)]

icon_sizes = ":".join(icon_sizes)

}
gtk-icon-sizes="$icon_sizes"

style "default"   
{ 
  engine "hcengine" {
    edge_thickness = 2
  }

  xthickness = 2
  ythickness = 2

# For Java Desktop System
  PanelMenu::stripe-gradient-top = "#000033"
  PanelMenu::stripe-gradient-bottom = "#000033"
  
  GtkWidget::interior-focus = 1
  GtkWidget::wide-separators = 0
  GtkWidget::separator-height = 2
  GtkWidget::separator-width = 2
  GtkRange::activate-slider = 1
  GtkArrow::arrow-size = 1.0
  GtkToolbar::shadow-type = GTK_SHADOW_NONE
  GtkToolbar::space-size = 30
  GtkProgressBar::min-horizontal-bar-height = 15
  GtkProgressBar::min-vertical-bar-width = 15

  GtkWidget::link-color = "#FFFFFF"
  GtkWidget::visited-link-color = "#FFCCFF"
  GtkWidget::focus-line-pattern = "\4\2"
  GtkWidget::focus-line-width = 5 
  GtkHSV::focus-line-pattern = "\0"
  GtkWidget::interior_focus = 1
  GtkWidget::focus-padding = 0
  GtkEntry::cursor_color    = "#FF0000" 
  GtkTextView::cursor_color    = "#FF0000"
  EelEditableLabel::cursor_color    = "#FF0000"
  GtkTextView::cursor_aspect_ratio = 0.3
  GtkEntry::cursor_aspect_ratio = 0.3
  EelEditableLabel::cursor_aspect_ratio = 0.3
  NautilusIconContainer::frame_text = 1
  GtkTreeView::expander-size = 32
  GtkRange::stepper-size = 20
  

  GtkCheckButton::indicator-size = 25
  
  fg[NORMAL]      = "#FFFFFF"
  text[NORMAL]    = "#FFFFFF"
  bg[NORMAL]      = "#000033" 
  base[NORMAL]    = "#000033"

  fg[INSENSITIVE]      = "#999999"
  bg[INSENSITIVE]      = "#333333"
  text[INSENSITIVE]      = "#999999"
  base[INSENSITIVE]      = "#333333"

  fg[PRELIGHT]    = "#000000"	
  text[PRELIGHT]    = "#003333"
  bg[PRELIGHT] = "#CCCC00"
  base[PRELIGHT]    = "#FFFFFF"

  fg[ACTIVE]      = "#FFFFFF"
  text[ACTIVE] = "#000000" 
  bg[ACTIVE]      = "#666699"
  base[ACTIVE]      = "#CCCC00"

  fg[SELECTED]    = "#000033"
  text[SELECTED]    = "#000033"
  bg[SELECTED]    = "#FFFFFF"
  base[SELECTED]    = "#CCCC00"


}

class "GtkWidget" style "default"

style "panel-icons"
{

}
class "GtkWidget" style "panel-icons"
style "media-icons"
{

}
class "GtkWidget" style "media-icons"

###########widget - details

style "window"
{

}

style "window-child"
{

}

style "white-bg"
{

}

style "white-bg-child"
{

}

style "black-bg"
{

}

style "black-bg-child"
{

}


style "groupbox-panel"
{

}

style "groupbox-panel-child"
{

}

style "groupbox-palette"
{

}

style "groupbox-palette-child"
{

}

style "menu"
{
    bg[PRELIGHT] = "#000033"

    GtkMenu::scroll-arrow-vlength = 25
    GtkMenu::horizontal-padding = 2
    GtkMenu::vertical-padding   = 2
    # This means the outline of the submenu overlaps with a palette.
    # However in the case of two normal menus, they are next to each other.
    # It is not possible to be smarter about this, because the style comes from
    # the submenu.
    GtkMenu::horizontal-offset  = 0
    GtkMenu::vertical-offset    = 0

    xthickness = 0
    ythickness = 0
}

style "palette-menu" = "menu"
{
    GtkMenu::horizontal-padding = 0
    GtkMenu::vertical-padding   = 0

    xthickness = 0
    ythickness = 15

    fg[NORMAL]="#FFFFFF"
}

# Can this all be moved in the menuitem style?
style "menu-child"
{
    fg[NORMAL]="#FFFFFF"
    base[NORMAL] = "#FFFFFF"

}



#########################################################
#########################################################


style "textview"
{
    text[NORMAL]="#000000"
    base[NORMAL]="#FFFFFF"

    GtkTextView::interior-focus = 1
}

style "scrollbar"
{
    fg[NORMAL]="#FFFFFF"
    fg[ACTIVE]="#FFFFFF"
    base[NORMAL]="#FFFFFF"
    base[ACTIVE]="#FFFFFF"
}

# hints for the trough padding hacks
# We cannot go trough GTK+, as we don't want a padding on all sides, but only one
# If we wanted padding on all sides, trough-border would work great.
style "hscrollbar" = "scrollbar"
{

}

style "vscrollbar" = "scrollbar"
{

}

style "hscrollbar-scrolled-window"
{
    
}

style "vscrollbar-scrolled-window"
{
  
}

style "scale"
{
    GtkWidget::focus-line-width = 0

    fg[NORMAL]="#FFFFFF"
    fg[ACTIVE]="#FFFFFF"  

    # "square" slider (really round of course)
    # Same as indicator-size?
    GtkRange::slider-width = 32
    GtkScale::slider-length = 32
    GtkRange::trough-border = 0
    GtkRange::stepper-spacing = 0
    GtkRange::trough-side-details = 1
}

# hints for the trough sizing hacks
style "hscale" = "scale"
{

}

style "vscale" = "scale"
{

}

style "spinbutton"
{
    xthickness = 15
    ythickness = 7
    GtkWidget::focus-line-width = 0
}


style "frame"
{

}

style "notebook-tab"
{
    fg[NORMAL] = "#FFFFFF"
}

style "notebook-panel"
{
   fg[NORMAL] = "#FFFFFF"
}

style "toolbox-notebook"
{
   fg[NORMAL] = "#FFFFFF"
}

style "toolbutton"
{
   fg[NORMAL] = "#FFFFFF"
}

style "separatortoolbutton"
{
    fg[NORMAL] = "#FFFFFF"
}

style "toolbar"
{

}

style "toolbox"
{
   fg[NORMAL] = "#000033"
}

style "panel"
{

}

style "entry"
{
    fg[NORMAL] = "#000000"
    base[NORMAL] = "#FFFFFF"
    text[NORMAL] = "#000000"
}

style "button"
{
    fg[NORMAL] = "#FFFFFF"
}

style "combobox"
{
    base[NORMAL] = "#FFFFFF"
}

style "comboboxentry"
{
    fg[NORMAL]="#FFFFFF" 
}

style "checkbutton"
{
   fg[NORMAL] = "#FFFFFF"
}

style "progressbar"
{

}

style "menuitem"
{
    GtkMenuItem::horizontal-padding = 0
    GtkMenuItem::arrow-spacing = 15
    GtkMenuItem::toggle-spacing = 15

    fg[NORMAL] = "#FFFFFF"

    xthickness = 15
    ythickness = 10
}

style "checkmenuitem"
{
    GtkCheckMenuItem::indicator-size = 26
    GtkMenuItem::toggle-spacing = 10
}

style "imagemenuitem"
{

}

style "separatormenuitem"
{
   fg[NORMAL] = "#FFFFFF"

   GtkWidget::wide-separators = 1
   GtkWidget::separator-height = 30

   ythickness = 0
   xthickness = 0
}

style "trayicon"
{
    
}

style "parent-bg"
{
    fg[NORMAL]="#FFFFFF"
    engine "sugar" {
        bg[NORMAL] = parent_bg_color
        bg[INSENSITIVE] = parent_bg_color
    }
}

style "label"{
	fg[NORMAL]="#FFFFFF"
}
style "hseparator"{
	fg[NORMAL]="#FFFFFF"
}
style "white_treeview"{
	fg[NORMAL]="#000000"
	/* base[NORMAL]="#000000" */
	text[NORMAL]="#000000"
	/* bg[NORMAL]="#000000" */
}

####################################################################
# Default style, setting some generic options and style properties
####################################################################
class "GtkWidget" style "default"


####################################################################
# Styles that apply the different background (and foreground) colors
####################################################################

# This one should probably be the default (ie. no window-child style)
widget_class "<GtkWindow>"               style "window"
widget_class "<GtkWindow>*"              style "window-child"

widget_class "*<SugarAlert>"               style "black-bg"
widget_class "*<SugarAlert>*"              style "black-bg-child"

widget_class "*<SugarSectionView>"       style "white-bg"
widget_class "*<SugarSectionView>*"      style "white-bg-child"


# The notebook is very high, so that everything is overriden
# Only the color of the tab labels needs to be modified inside the
# notebooks in this style (and the widget itself).
# Assume that there is either just a normal label in the notebook tab, or
# it is inside a GtkBox (H- or VBox) together with eg. a close button.
widget_class "*<GtkNotebook>"                        style "notebook-tab"
widget_class "*<GtkNotebook>.<GtkLabel>"             style "notebook-tab"
widget_class "*<GtkNotebook>.<GtkBox>.<GtkLabel>"    style "notebook-tab"


# SugarPalette and Menu
widget_class "*<GtkMenu>"               style "menu"
widget_class "<SugarPalette>"           style "menu"
widget_class "<SugarPalette>.*"         style "menu-child"
widget_class "<SugarPalette>*<GtkMenu>" style "palette-menu"
widget_class "*<GtkMenuShell>.*"        style "menu-child"

# SugarFrameWindow
widget_class "*<SugarFrameWindow>*"    style "frame"

# SugarPanel
widget_class "*<SugarPanel>*"          style "panel"


# GroupBoxes (don't set bg[NORMAL] on the widget itself)
widget_class "<GtkWindow>*<SugarGroupBox>*"   style "groupbox-panel-child"

widget_class "<GtkWindow>*<GtkNotebook>*"   style "groupbox-panel-child"
widget_class "<GtkWindow>*<GtkNotebook>"    style "notebook-panel"


widget_class "<SugarPalette>*<SugarGroupBox>*"   style "groupbox-palette-child"


# SugarToolbox
#widget_class "*<SugarToolbox>" style "toolbox"
#widget_class "*<SugarToolbox>*" style "toolbox-child"
#widget_class "*<SugarToolbox>*<GtkEventBox>" style "toolbox"
#widget_class "*<SugarToolbox>*<GtkLayout>"   style "toolbox"
widget_class "*<SugarToolbox>*"        style "toolbox"
widget_class "*<GtkToolbar>*"          style "toolbox"
widget_class "*<SugarToolbox>.<GtkNotebook>" style "toolbox-notebook"


####################################################################
# Normal widget styles, using the above things
####################################################################
# The following only uses widget_class matches to get the priority
# right. An alternative would be to lower the priority of the
# background matches (which need widget_class) to eg. "application"

widget_class "*<GtkMenuItem>*"            style "menuitem"
widget_class "*<GtkCheckMenuItem>"        style "checkmenuitem"
widget_class "*<GtkImageMenuItem>"        style "imagemenuitem"
widget_class "*<GtkSeparatorMenuItem>*"   style "separatormenuitem"

# Buttons and Combos
widget_class "*<GtkButton>*"           style "button"
widget_class "*<GtkCheckButton>*"      style "checkbutton"
widget_class "*<GtkComboBox>*"         style "combobox"
widget_class "*<GtkComboBoxEntry>*"    style "comboboxentry"
widget_class "*<GtkCombo>*"            style "comboboxentry"

# Entries
widget_class "*<GtkEntry>"       style "entry"
widget_class "*<GtkSpinButton>"  style "spinbutton"
widget_class "*<GtkTextView>"    style "textview"


# Misc widgets
widget_class "*<GtkHScrollbar>"  style "hscrollbar"
widget_class "*<GtkVScrollbar>"  style "vscrollbar"
widget_class "*<GtkHScale>"      style "hscale"
widget_class "*<GtkVScale>"      style "vscale"
widget_class "*<GtkProgressBar>" style "progressbar"

# Scrolled window scrollbars
widget_class "*<GtkScrolledWindow>.<GtkVScrollbar>" style "vscrollbar-scrolled-window"
widget_class "*<GtkScrolledWindow>.<GtkHScrollbar>" style "hscrollbar-scrolled-window"

# Toolbar
widget_class "*<GtkToolButton>*"          style "toolbutton"
widget_class "*<GtkSeparatorToolItem>*"   style "separatortoolbutton"
widget_class "*<GtkToolbar>"              style "toolbar"

# Tray
widget_class "*<SugarTrayIcon>*" style "trayicon"

# Widgets that should get the background color from the parent
widget_class "*<GtkEventBox>"        style "parent-bg"
widget_class "*<GtkLayout>"          style "parent-bg"
widget_class "*<GtkViewport>"        style "parent-bg"
widget_class "*<GtkDrawingArea>"     style "parent-bg"
widget_class "*<GtkScrolledWindow>"  style "parent-bg"

widget_class "*<GtkLabel>*"	     style "label"
widget_class "*<GtkHSeparator>*"      style "hseparator"

widget_class "*<JournalTreeView>*" style "white_treeview"
widget_class "*<SugarActivitiesTreeView>*" style "white_treeview"
