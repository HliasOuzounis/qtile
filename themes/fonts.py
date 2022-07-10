"""
file containing a selection of possible sets of fonts
"""
# singular fonts
victormono = {
    "font": "VictorMono Nerd Font Semibold",
    "fontsize": 16,
    "padding": 3
}

comiccode = {
    "font": "Comic Code",
    "fontsize": 14,
    "padding": 0,
}

comiccode_large = {
    "font": "Comic Code",
    "fontsize": 16,
    "padding": 0,
}

cozette = {
    "font": "CozetteVector",
    "fontsize": 24,
    "padding": 0
}

firacode = {
    "font": "FiraCode Nerd Font Mono",
    "fontsize": 14,
    "padding": 3
}


firacode_large = {
    "font": "FiraCode Nerd Font Mono",
    "fontsize": 22,
    "padding": 3
}

source_pro = {
    "font": "Source Code Pro",
    "fontsize": 14,
    "padding": 2
}
# font sets
all_victormono = {
    "clear": victormono,
    "mono": victormono,
    "secondary": victormono
}

all_firacode = {
    "clear": firacode_large,
    "mono": firacode,
    "secondary": firacode
}

all_comiccode = {
    "clear": firacode_large,
    "mono": comiccode,
    "secondary": comiccode
}

all_source_pro = {
    "clear": source_pro,
    "mono": source_pro,
    "secondary": source_pro,
}
# selected font set
font = source_pro