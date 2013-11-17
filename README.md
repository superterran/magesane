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

Comparison
----------

    Without providing any real facts, here's an idea of what to expect:

    Full DB dumps
    -------------

    Popular Client Involving Phone Cases:
        Original: ~4.8GB
        Sanitized: ~1.6GB //no customer or log data

    Popular Client Involving bags with awesome patterns:
        Original: ~280MB
        Sanitized: ~150MB //no customer or log data

Installation
------------

    Mark magesane as executable, and then symlink to a path like /usr/local/bin

Requirements
------------
    Python 2.6+ (tested)
