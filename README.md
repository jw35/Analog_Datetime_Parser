This module contains a single function `parse()` that understands the formats
used by the late-lamented 'Analog' web server analysis program
(https://web.archive.org/web/20130806225209/http://www.analog.cx:80/) for its
'FROM' and 'TO' commands. These dates can be absolute, representing a fixed
moment in time, or relative to some other date which defaults to 'now', or any
combination of the two. This turns out to be useful for scheduling
periodic, date-related processing such as analysing log files because it lets
you specify things like 'last month' using fixed strings.

The dates parsed by this module differ from those processed by Analog in
always using 4 digits for years (two digit years are immoral).

The simplest use of this format is `yyyyMMdd` or `yyMMdd:hhmm`, where `yyyy`
represents the year, `MM` represents the month, `dd` is the date, `hh` the
hour, and `mm` the minute. So, for example, to analyse only requests from 1st
July 1999 to 1pm on 15th June 2000 you could use the configuration

    FROM 19990701
    TO   20000615:1300

Alternatively, each of the components can be preceded by `+` or `-` to
represent time relative to some other time, defaulting to 'now'. In this case,
years can have more than 4 digits (though that's unlikely and they still need
to have at least 4) and the other components can have more than 2 digits. This
allows constructions like

    FROM -0001-00+01         # from tomorrow last year
    TO   -0000-0131          # to the end of last month (OK even if last month
                             # didn't have 31 days)
    FROM -0000-00-112
    TO   -0000-00-01         # statistics for the last 16 weeks

    FROM -0000-00-00:-06+01  # statistics for the last 6 hours

### `parse(date, base=datetime.now())`

Given an appropriate `date`, this function returns a new
`datetime.datetime` object.  If `date` contains relative elements then they will
be calculated relative to `base` which defaults to `datetime.datetime.now()`.

If given an improperly formatted string, this method will raise `ValueError`.
But beware that it's easy to create strings that parses, but not the way
you expect! This module always interprets day numbers that are too large
for the corresponding month as representing the last day of the month.
