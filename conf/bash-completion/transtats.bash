# transtats bash completion

_transtats()
{
    COMPREPLY=()

    in_array()
    {
        local i
        for i in $2; do
            [[ $i = $1 ]] && return 0
        done
        return 1
    }

    local cur prev
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # global options
    local options="--help"
    local options_value=
    local commands="coverage package release version"

    # parse main options and get command
    local command=
    local command_first=
    local path=

    local i w
    for (( i = 0; i < ${#COMP_WORDS[*]} - 1; i++ )); do
        w="${COMP_WORDS[$i]}"
        # option
        if [[ ${w:0:1} = - ]]; then
            if in_array "$w" "$options_value"; then
                ((i++))
                [[ "$w" = --path ]] && path="${COMP_WORDS[$i]}"
            fi
        # command
        elif in_array "$w" "$commands"; then
            command="$w"
            command_first=$((i+1))
            break
        fi
    done

    # complete base options
    if [[ -z $command ]]; then
        if [[ $cur == -* ]]; then
            COMPREPLY=( $(compgen -W "$options $options_value" -- "$cur") )
            return 0
        fi

        case "$prev" in
            *)
                COMPREPLY=( $(compgen -W "$commands" -- "$cur") )
                ;;
        esac

        return 0
    fi

    # parse command specific options
    local options="--json --server-url --help"
    local options_release= options_version=
    local after= after_more=

    case $command in
        release)
            options_release="--detail "
            ;;
        version)
            options_version="--server"
            ;;
    esac

    local all_options="--help $options"
    local all_options_value="$options_release $options_version"

    # count non-option parameters
    local i w
    local last_option=
    local after_counter=0
    for (( i = $command_first; i < ${#COMP_WORDS[*]} - 1; i++)); do
        w="${COMP_WORDS[$i]}"
        if [[ ${w:0:1} = - ]]; then
            if in_array "$w" "$all_options"; then
                last_option="$w"
                continue
            elif in_array "$w" "$all_options_value"; then
                last_option="$w"
                ((i++))
                continue
            fi
        fi
        in_array "$last_option" "$options_arches" || ((after_counter++))
    done

    # completion
    if [[ -n $options_release ]] && in_array "$prev" "$options_release"; then
        COMPREPLY=( )
    elif [[ -n $options_version ]] && in_array "$prev" "$options_version"; then
        COMPREPLY=( )
    else
        local after_options=

        if [[ $cur != -* ]]; then
            all_options=
            all_options_value=
        fi

        COMPREPLY+=( $(compgen -W "$all_options $all_options_value $after_options" -- "$cur" ) )
    fi

    return 0
} &&
complete -F _transtats transtats

