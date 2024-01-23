==========
 Overview
==========

Ivy is a lightweight software bus for quick-prototyping protocols. It
allows applications to broadcast information through text messages, with a
subscription mechanism based on regular expressions.

The Ivy software bus was designed at the French Centre d'Études de la
Navigation Aérienne (CENA).  The original work: software, documentation,
papers, credits can be found on the `Ivy Home Page`_; it contains all the
necessary materials needed to understand Ivy.

This package is the Python library; Ivy libraries are also available for
numerous languages, among which: C, C#, C++, Java, Perl --see the `Ivy Download
Page <https://www.eei.cena.fr/products/ivy/download/index.html>`_ for details.

This python library is a full rewrite of the original software, and it is
written in pure python.  Note that another python implementation is available
at the `Ivy downloads page`_, which is built by `SWIG <http://www.swig.org/>`_
on top of the Ivy C library.

Why choosing the Ivy bus?
=========================

They are a lot of other software libraries making messaging possible between applications.

The Ivy bus itself was designed to allow quick prototyping of protocols, and with it you will find it easy to even extend existing applications to interact with each other in their own native language.  The characteristics of protocols built with the Ivy bus are the following:

- messages are text only,
- subscriptions are made of regexps,
- messages are delivered immediately to the subscribers,
- there is no server: every participant on the bus knows every other one.


.. _Ivy Home Page: https://www.eei.cena.fr/products/ivy/
.. _The Ivy C library: https://www.eei.cena.fr/products/ivy/documentation/ivy-c.pdf
.. _Ivy downloads page: https://www.eei.cena.fr/products/ivy/download/binaries.html
