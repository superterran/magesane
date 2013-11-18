MageSane
========
superterran@gmail.com

MageSane is a simple sql dump sanitizer for Magento aimed to speed up database imports and
reduce filesystem footprints. DB sanitizers floating around are generally a series of update and truncate
statements fired after a full import operation. This is time consuming and doesn't always release filesystem space
on many standard mysql setups.

Instead, pipe a full db dump through magesane and the file is sanitized before MySQL imports, resulting in a
significantly faster import, smaller overall file size and better database performance. MageSane will also disable
foreign key constraints, strip out any trigger definers, and provide options for further sanitation like ofuscating
customer data, or choosing to not import customer/order/catalog data at all.

Usage
-----

Usage: magesane [options]

Options:
  -h, --help            show this help message and exit
  -r INPUTFILE, --read=INPUTFILE
                        which file to read, can also pass as first argument or
                        as pipe
  -o OUTPUTFILE, --output=OUTPUTFILE
                        where to save, by default this outputs to buffer
  -i ignoreprofiles, --ignore=ignoreprofiles
                        pass in custom ignore list, comma separated. Use
                        profiles i.e. logs,sales,customer
  -a addins, --addin=addins
                        adds custom statements to end of dump, comma separated
                        defined in ini

Usage Examples
--------------

    Here's a few ways you can use the script, depending on your needs:

    * import via mysql client: magesane source.sql | mysql -uroot database
    * import via mysql client, only ignore logs: magesane -i log source.sql| mysql -uroot database

    * run file, save new: magesane -r source.sql -o destination.sql
    * run file, save new: magesane source.sql > destination.sql
    * run file, save new: cat source.sql | magesane > destination.sql

Comparison
----------

    Without providing any real facts, here's an idea of what to expect:

    Full DB dumps
    -------------

    Popular Client Involving Phone Cases
        Original: 4.8GB
        Sanitized: 1.6GB //no customer or log data

    Popular Client Involving bags with awesome patterns:
        Original: 297MB
        Sanitized: 149MB //no customer or log data

Installation
------------

    Mark magesane as executable, and then symlink to a path like /usr/local/bin
ex
Requirements
------------
    Python 2.6+ (tested)
    python2-configglue (arch) for ConfigParser
