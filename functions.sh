#!/bin/bash
# Here you can create functions which will be available from the commands file
# You can also use here user variables defined in your config file
# To avoid conflicts, name your function like this
# pg_XX_myfunction () { }
# pg for PluGin
# XX is a short code for your plugin, ex: ww for Weather Wunderground
# You can use translations provided in the language folders functions.sh
siri_start() {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    jv_debug "Starting Siri Notes Listener..."
    $verbose && local quiet="--verbose" || local quiet="" 
    python $DIR/main.py \
        --username "$siri_gmail_username" \
        --password "$siri_gmail_password" \
        --interval "$siri_check_interval" \
        $quiet &
}
