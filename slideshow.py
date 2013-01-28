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

import random, os, PIL.Image as Image
from glob import glob

# dummy dictionary replacing Zookeepr config
file_paths = {
    'public_html': 'test_data/html',
    'public_path': 'test_data/path',
}

def slideshow(set, small=None):
    """
    Generate a slideshow of a set of images, randomly selecting one to
    show first, unless a file is specified.

    @param set: (cough) string representing a directory name under /images/
    @param small: string representing a filename under /images/{set}/small/
    @returns: A string containing html with a div that has slideshow functionality.
    """
    try:
        if small == None or small == "":
            # Randomly select a smaller image, set the width of the div to be
            # the width of image.
            small = random.choice(glob(file_paths["public_path"] + "/images/" + set + "/small/*"))
        else:
            small = file_paths["public_path"] + "/images/" + set + "/small/" + small

        output = "<div class=\"slideshow\" id=\"%s\" style=\"width: %dpx\">" % (set, int(Image.open(small).size[0]))
        small = os.path.basename(small)

        # Optionally load up some captions for the images.
        caption = dict()
        caption_file = file_paths['public_path'] + "/images/" + set + "/captions"
        if os.path.exists(caption_file):
            file = open(caption_file, 'r')
            captions = file.readlines()

            # Assign captions to a lookup table
            for cap in captions:
                str = cap.partition(':')
                caption[str[0]] = str[2]

        # Load up all the images in the set directory.
        files = glob(file_paths['public_path'] + "/images/" + set + '/*')
        for file in files:
            if os.path.isfile(file):
                short_file = os.path.basename(file)
                if short_file == 'captions':
                    continue

                output += "<a href=\"" + file_paths["public_html"] + "/images/" + set + "/" + short_file + "\" rel=\"lightbox[" + set + "]\""
                if short_file in caption:
                    output += " title=\"" + caption[short_file] + "\""
                output += ">"

                # If we're looking at the small one we've picked, display
                # it as well.
                if short_file == small:
                    output += "<img src=\"" +  file_paths["public_html"] + "/images/" + set + "/small/" + short_file + "\">"

                    # If there are more than one image in the slideshow
                    # then also display "more...".
                    if files.__len__() > 1:
                        output += '<div class="more">More images...</div>'
                output += "</a>\n";
        output += "</div>\n"
        return output

    except IndexError:
        return "no images found"
