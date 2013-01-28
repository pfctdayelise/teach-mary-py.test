"""
    This file is part of Teach Mary py.test.

    Teach Mary py.test is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Teach Mary py.test is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Teach Mary py.test.  If not, see <http://www.gnu.org/licenses/>.
"""

def ticket_percentage_text(percent, earlybird = False):
    if percent == 100:
        return 'All tickets gone.'
    elif percent >= 97.5:
        if earlybird:
            return "Earlybird almost soldout."
        else:
            return "Almost all tickets gone."
    else:
        if earlybird:
            return "%d%% earlybird sold." % percent
        else:
            return "%d%% tickets sold." % percent

