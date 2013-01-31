

* {
    -sugar-focus-line: @white;

    /* A lot of these will probably need to be changed, but this has to
       be done when the exact sizes are known */
    -GtkWidget-interior-focus: 0;

    /* we have to disable focus border for GtkTreeView, see #1261 */
    -GtkTreeView-interior-focus: 1;
    -GtkTreeView-focus-line-width: 0;

    -GtkTextView-interior-focus: 1;

    -GtkWidget-focus-line-width: 0;  /* Prevents some drawing glitches */
    -GtkEntry-focus-line-width: 0;
    -GtkScale-focus-line-width: 0;
    -GtkWidget-focus-padding: 0;
    /* 0.05 works good for both the sugar and sugar-xo themes */
    -GtkWidget-cursor-aspect-ratio: 0.05;

    -GtkWidget-wide-separators: true;
    -GtkWidget-separator-height: 2;
    -GtkWidget-separator-width: 2;

    -GtkWidget-scroll-arrow-hlength: 11;
    -GtkWidget-scroll-arrow-vlength: 11;

    -GtkRange-activate-slider: 1;

    /* We fake the default border in the theme */
    -GtkButton-default-border: 0 0 0 0;
    -GtkButton-default-outside-border: 0 0 0 0;
    -GtkButton-image-spacing: 11;

    -GtkEntry-progress-border: 2 2 2 2;

    -GtkScrolledWindow-scrollbar-spacing: 0;

    -GtkExpander-expander-size: 17;
    -GtkExpander-expander-spacing: 2;

    -GtkTreeView-expander-size: 17;

    -GtkArrow-arrow-size: 1.0;

    -GtkToolbar-space-size: 22;
    -GtkToolbar-shadow-type: none;

    -GtkProgressBar-min-horizontal-bar-height: 11;
    -GtkProgressBar-min-vertical-bar-width: 11;

    -GtkButtonBox-child-min-height: 33;
    -GtkButtonBox-child-min-width: 33;
    -GtkButtonBox-child-internal-pad-x: 0;
    -GtkButtonBox-child-internal-pad-y: 0;

    -GtkCheckButton-indicator-size: 26;
    -GtkCheckButton-indicator-spacing: 3;

    -GtkWidget-text-handle-width: 110px;
    -GtkWidget-text-handle-height: 110px;
}

* {
    border-color: @white;
}

*:insensitive {
    color: @button_grey;
}

*:hover {
    background-color: #CCCC00;
}

/* Backgrounds and windows */

GtkWindow {
    background-color: @black;
    color: @black;
}

GtkDialog {
    background-color: @black;
    color: @white;
}

SugarIntroWindow {
    background-color: @white;
}

SugarIntroWindow {
    color: @black;
}

GtkLabel, GtkLabel:insensitive {
    background-color: transparent;
    color: @white;
}

/* Buttons */

.button {
    
    /* It would be nicer to just set the inner-border, but that does not work
       for combo boxes ... The combobox ignores it, so set it to 0px
       See http://bugzilla.gnome.org/show_bug.cgi?id=485762 */

    -GtkButton-inner-border: 0 0 0 0;
    padding: 5px 5px 5px 5px;

    border-width: 2px;
    border-style: solid;
    color: @white;
}

.button:focused {
    border-color: @white;
}

.button:active:focused {
    color: @black;
}

/* Spin buttons */

.spinbutton.button {
    border-radius: 0px;
    border-width: 0px;
    border-style: solid;
}

.spinbutton.button:last-child {
    border-width: 0px 0px 0px 2px;
    border-style: solid;
}


/* Toggle buttons */

GtkToggleButton.button:active {
    color: @black;
}

/* Entries and views */

.view {
    border-width: 0px;
    border-style: none;
    border-radius: 0px;
    padding: 0px;
    background-color: @white;
}

GtkTreeView {
    background-color: @button_grey;
}

GtkTreeView row:nth-child(even) {
    background-color: @row_even;
}
GtkTreeView row:nth-child(odd) {
    background-color: @row_odd;
}

.entry {
    border-width: 2px;
    border-style: solid;
    background-color: @white;
    color: @black;
    
    
    padding: 6px 8px 6px 8px;
}

.entry.progressbar {
    border-width: 2px;
    background-color: @selection_grey;
}

.entry:focused {
    background-color: @white;
}

.toolbar .entry:focused {
    border-color: @white;
}

.entry:insensitive, .view:insensitive {
    background-color: @button_grey;
}


.view:selected {
    background-color: @panel_grey;
    color: @black;
}

.view:insensitive {
    background-color: @white;
    color: @black;
}

.entry:selected,
.entry:selected:focused,
.view:selected:focused {
    background-color: @selection_grey;
    color: @black;
}


/* Frames */

GtkScrolledWindow.frame {
    border-style: solid;
    border-width: 2px;
    border-radius: 0;
    padding: 4px;
}

GtkFrame.frame.journal-preview-box {
    border-style: solid;
    border-width: 2px;
}

/* Combo boxes */

GtkComboBox {
    color: @white;
    border-color: @white;
}

GtkComboBox .separator {
    /* Remove the separator turning it transparent */
    color: alpha(@theme_base_color, 0.0);
}

/* Notebooks */

.notebook {
    background-color: @selection_grey;
    color: @black;
    padding: 0px;
    -GtkNotebook-tab-overlap: -2;
    -GtkNotebook-tab-curvature: 4;
}

.notebook tab {
    background-color: @selection_grey;
}

/* Setting white color to the tab labels using only the previous rule */
/* doesn't work, so we have to set white color to the GtkLabel, and make */
/* sure the buttons get black color in the next two rules: */
.notebook tab GtkLabel {
    color: @white;
    padding: 11px 0;
}

.notebook tab .button GtkLabel {
    color: @black;
}

.notebook tab:active {
    background-color: @black;
}


/* Browse Widgets */

BrowseTabPage {
    background-color: @black;
}

BrowseSearchWindow .view {
    background-color: @black;
    color: @white;
    border-width: 0 2px 2px 2px;
    border-style: solid;
}

/* Control panel */

SugarSectionView {
    background-color: @white;
    color: @black;
}

SugarSectionView *:insensitive {
    background-color: @white;
}

/* Alert */

SugarAlert {
    background-color: @black;
    color: @white;
}

SugarAlert *:insensitive {
    background-color: @black;
}

.button SugarTimeoutIcon GtkLabel,
.button SugarTimeoutIcon GtkLabel:prelight {
    background-color: @white;
    color: @button_grey;
}

.button SugarTimeoutIcon GtkLabel:active {
    background-color: @toolbar_grey;
    color: @white;
}

/* Tray */

SugarHTray, SugarVTray {
    background-color: @toolbar_grey;
}

SugarHTray * , SugarVTray * { background-color: @toolbar_grey;}

/* Menus and palettes */

SugarPaletteWindowWidget {
    border-width: 2px;
    border-style: solid;
    background-color: @black;
    color: @white;
}

SugarPaletteWindowWidget .view {
    color: @black;
}

SugarPaletteMenuWidget {
    background-color: @black;
}

SugarPaletteMenuWidget * {
    color: @white;
}


SugarPaletteWindow SugarGroupBox {
    background-color: @toolbar_grey;
    color: @white;
}

SugarPaletteWindow SugarGroupBox *:insensitive {
    background-color: @toolbar_grey;
}

.menu {
    color: @white;

    -GtkMenu-scroll-arrow-vlength: 19;
    -GtkMenu-horizontal-padding: 2;
    -GtkMenu-vertical-padding  : 2;
    /* This means the outline of the submenu overlaps with a palette.
     * However in the case of two normal menus, they are next to each other.
     * It is not possible to be smarter about this, because the style comes from
     * the submenu. */
    -GtkMenu-horizontal-offset : 0;
    -GtkMenu-vertical-offset   : 0;

    padding: 0px 0px 11px 0px;
    border-width: 2px;
    border-style: solid;
}

.menu :active {
    background-color: @button_grey;
}

.menuitem {
    padding: 11px 8px;
}

.menuitem.separator {
    padding: 11px 0px;
}

SugarPaletteHeader.menuitem {
    padding: 0px 8px;
}

SugarPaletteHeaderSeparator.menuitem.separator {
    padding: 0px 0px 11px 0px;
}

.tooltip {
    border-style: solid;
    border-width: 2px;
}

.tooltip * {
    color: @white;
}

/* Scrollbars */

.scrollbar {
    -GtkRange-slider-width: 11;
    -GtkRange-trough-border: 0;
    -GtkRange-stepper-size: 0;
    -GtkScrollbar-min-slider-length: 33;
    -GtkScrollbar-has-forward-stepper: 0;
    -GtkScrollbar-has-backward-stepper: 0;
    -GtkScrollbar-has-secondary-forward-stepper: 0;
    -GtkScrollbar-has-secondary-backward-stepper: 0;
}

.scrollbar.trough {
    background-color: @button_grey;
    border-width: 0px;
}

.scrollbar.slider {
    background-color: @white;
    border-width: 0px;
}

.scrollbar.slider:active {
    background-color: @text_field_grey;
}

/* Progress bars */

/* Scrollbar padding hack? What was that about? */

GtkProgressBar.progressbar {
    background-color: @white;
    border-style: solid;
    border-width: 2px;
}

GtkProgressBar.trough {
    background-color: @selection_grey;
    border-style: solid;
    border-width: 2px;
}

.toolbar GtkProgressBar.trough,
SugarPaletteWindowWidget GtkProgressBar.trough {
    background-color: @black;
}

/* Separators */

.separator {
    border-style: solid;
    border-width: 2px;
}

/* Tool buttons */

.toolbar {
padding: 0px;
background-color: @toolbar_grey;
color: @white;
}

.toolbar .button,
SugarPaletteWindowWidget SugarRadioToolButton .button {
    border-radius: 0px;
    border-style: none;
}

.toolbar .button #gtk-toolbar-arrow {
    padding: 0 15px;
}

.toolbar GtkToolButton .button,
.toolbar SugarRadioToolButton *,
SugarPaletteWindowWidget SugarRadioToolButton *,
SugarPaletteWindowWidget GtkToolButton .button {
    padding: 7px;
}

.toolbar GtkToolButton .button,
SugarPaletteWindowWidget GtkToolButton .button:prelight {
    padding: 3px;
    border-width: 4px;
    border-style: solid;
    background-clip: padding-box;
}


.toolbar GtkToolButton .button:active {
}

SugarPaletteWindowWidget GtkScrolledWindow * {
    background-color: @black;
}


/* Scales */

.scale {
    -GtkScale-slider-length: 24;
    -GtkRange-slider-width: 24;
}

/* We have to override the color of the scale, otherwise the slider
   background image is invisible or not set for this palettes.
   Upstream bug: https://bugzilla.gnome.org/show_bug.cgi?id=686703 */
SugarPaletteWindowWidget .scale {
    color: transparent;
}

.scale.trough {
    background-color: @button_grey;
    border-style: solid;
    border-width: 2px;
    margin: 8px 0;
}

.scale.trough.vertical {
    margin: 0 8px;
}


.scale.trough.top,
.scale.trough.left {
    background-color: @white;
}

.scale.trough.top:focused,
.scale.trough.left:focused {
}


.scale.slider,
.scale.slider:active {
    background-color: transparent;
}

.scale.slider {
    background-image: url("assets/scale-slider.svg");
}

.scale.slider:active {
    background-image: url("assets/scale-slider-active.svg");
}

/* Radio and check buttons */

GtkCheckButton:prelight {
    background-color: alpha(@theme_base_color, 0.0);
}

.toolbar GtkCheckButton,
SugarPaletteWindowWidget GtkCheckButton {
    color: @theme_base_color;
}

.radio,
.radio row:selected,
.radio row:selected:focused {
    background-image: url("assets/radio.svg");
}

.radio:selected,
.radio:selected row:selected,
.radio:selected row:selected:focused {
    background-image: url("assets/radio-selected.svg");
}

.radio:active,
.radio row:selected:active,
.radio row:selected:focused:active {
    background-image: url("assets/radio-active.svg");
}

.radio:active:selected,
.radio:selected row:selected:active,
.radio:selected row:selected:focused:active {
    background-image: url("assets/radio-active-selected.svg");
}

.check,
.check row:selected,
.check row:selected:focused {
    background-image: url("assets/checkbox-unchecked.svg");
}

.check:selected,
.check:selected row:selected,
.check:selected row:selected:focused {
    background-image: url("assets/checkbox-unchecked-selected.svg");
}

.check:active,
.check row:selected:active,
.check row:selected:focused:active {
    background-image: url("assets/checkbox-checked.svg");
}

.check:active:selected,
.check:selected row:selected:active,
.check:selected row:selected:focused:active {
    background-image: url("assets/checkbox-checked-selected.svg");
}

/* Tool items */

.toolitem {
    /* arrow in the toolbarbox */
    color: @white;
    /* outline of the toolbarbutton when palette is expanded */
    border-style: solid;
    border-width: 2px;
}

/* GtkImage */

GtkImage {
    background-color: transparent;
}

/* Sugar Frame Window */

SugarFrameWindow {
    background-color: @toolbar_grey;
}

/* Sugar Canvas icon */

SugarCanvasIcon,
SugarKeepIcon.button {
    border-width: 2px;
    border-style: solid;
}

SugarCanvasIcon:prelight,


/* Sugar CellRenderer Icons */

.cell.sugar-icon-cell {
    border-width: 2px;
    border-style: solid;
}


/* Text cursor handles */

.cursor-handle.top,
.cursor-handle.bottom {
    box-shadow: none;
    border-style: none;
    border-image: none;
    border-radius: 0px;
    border-width: 0px;
}

.cursor-handle.bottom {
    background-image: url("assets/cursor-handle-bottom.svg");
}

.cursor-handle.top {
    background-image: url("assets/cursor-handle-top.svg");
}

.cursor-handle.insertion-cursor {
    background-image: url("assets/cursor-handle-insertion.svg");
}

/* Application specific properties */

EvView {
    background-color: @panel_grey;
}

EvView:selected,
ApDocView:selected {
    background-color: @selection_grey;
}

/* Application specific properties */

EvView {
    background-color: @panel_grey;
}

EvView:selected,
ApDocView:selected {
    background-color: @selection_grey;
}
