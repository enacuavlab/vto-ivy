==========
 Tutorial
==========

Preparation
-----------

ivy-python is a message bus, so to demonstrate its usage, we will need
two agents on the bus for them to exchange messages.

| Fortunately, ivy-python ships with an already full-featured, generic agent called `ivyprobe.py`.
| To follow this tutorial, you need to open two terminals next to one another.

Let's open a new terminal, and launch ``ivyprobe.py``::

    $ ivyprobe.py -s hi 'ivyprobe (.*)'
    Broadcasting on ivydefault
    Go ahead! (type .help for help on commands)
    Changes in applications' bindings are now shown

What this command does is:

- it creates a new agent, name "pyivyprobe", on the standard ivy bus.

- this agent registers two subscriptions: one for messages being
  exactly "hi", and the other one for messages corresponding to the
  regular expression "Hello (.*)".  We will explain these concepts below.

| This gives us an agent to discuss with from ivy-python.
| Note that this generic agent, shipped with ivy-python, can be very handy to look at what happens on an Ivy bus.

Also note that ``ivyprobe`` indifferently use the terms 'subscriptions" or "bindings" when speaking about subscriptions to messages. This is explained in the section `Subscribing to messages`_, below.


Creating a new agent
--------------------

Now, open, a new terminal, and launch `python`, then type:


  .. code-block:: python
     :name: tuto_create_agent

     >>> from ivy.std_api import *
     >>> IvyInit("my agent")
     >>> IvyStart()

We have just created out first agent, named ``my_agent`` and connected it to the bus.
Looking at the terminal where ``ivyprobe`` is launched, you see it appeared on the bus:

.. code-block:: none
   :caption: ivyprobe

   Ivy application 127.0.0.1:38079 (my_agent) has connected
   Ivy applications currently on the bus: my_agent


Subscribing to messages
-----------------------

Our first subscription
++++++++++++++++++++++

Agents only receive messages they subscribed for.  The subscription mechanism is based on regular expression. It can be:

- a simple text, like "hi!": when someone on the bus sends this exact string, the agent receives it,
- a regular expression, like "hello .*": any message sent on the bus and matching the regular expression is received by our agent.

Let's declare our first subscription:

.. code-block:: python
   :name: tuto_register_subscription_hi
   :linenos:

   >>> def on_hi(agent):
   ...     print("Agent %r sent hi!"%agent)
   ...
   >>> IvyBindMsg(on_hi, "hi!")
   0

There are several things to note here.

- The lines 1-2 declare a *callback*: this is the function that will be called when the message is received. Callbacks are an important concept: almost everything happening on the bus triggers a callback that was previously bound to a particular event.

- On line 4, we bind this callback to the definition of the message, here the simple string "hi!".

- Line 5: ``IvyBindMsg()`` returns an integer (0), which is the *index* of the new registered *binding* (or *subscription*).  This index can be used to remove a subscription later, using ``IvyUnBindMsg()``.


Now if you look at the terminal where ``ivyprobe.py`` is running, it should display something like this:

.. code-block:: none
   :caption: ivyprobe

   Ivy application 127.0.0.1:56981 (my_agent) has connected
   Ivy applications currently on the bus: my_agent
   127.0.0.1:56981 (my_agent) added regexp id=0: hi!

showing that:

- it detected the connection of our new agent,
- it registered the new subscription.

Now you can use ``ivyprobe`` to send to try to send message on the bus.  In ``ivyprobe``, everything you type is directly sent on the bus (except for recognized commands).

So, in the terminal where ``ivyprobe`` runs, type: ``hi!`` and hit return.  It displays:

.. code-block:: none
   :caption: ivyprobe

   hi!
   Sent to 1 peers

``ivyprobe`` indicates the number of agents (*peers*) the message was sent to.
Plus, on the terminal where python runs, the following message was displayed::

  Agent 127.0.0.1:43370 (pyivyprobe) sent hi!

Our callback function, ``on_hi()`` was called and it printed the message.  We have successfully registered a subscription and received our first message!

Before going further, you can try to send other messages from ``ivyprobe``, such as ``hello``, ``hi`` or ``Hi!``: ivyprobe always says::

    Sent to 0 peers

and indeed, our python agent do not receive any of these messages.


**Subscriptions and bindings** To *subscribe* to a message, an agent
  *binds* a callback function to a regular expression a function.
  This is why in "Ivy speaking" both terms "subscriptions" and
  "bindings" are synonyms, and we use them indifferently.


Using regular expressions
+++++++++++++++++++++++++

In Ivy, a subscription is declared using a regular expression, or *regexp*.

.. note:: We suppose that the reader is already familiar with his concept.  If not, you will find numerous introductory materials on the internet.  We suggest the `Regular Expression HOWTO <https://docs.python.org/3/howto/regex.html#regex-howto>`_ on python.org.

Let's subscribe to all messages starting with "Hello ":

.. code-block:: python
   :name: tuto_register_subscription_hello

   >>> def on_hello(agent):
   ...     print("Agent %r said hello"%agent)
   ...
   >>> IvyBindMsg(on_hello, "Hello .*")
   1

Looking at the terminal where ``ivyprobe`` runs, you can see that the new subscriptions was registered as well.  From ``ivyprobe``, send the string ``Hello World!``:

.. code-block:: none
   :caption: ivyprobe

   Hello World!
   Sent to 1 peers

| Our python agent displays ``Agent 127.0.0.1:55458 (pyivyprobe) said hello``: the message was successfully delivered..
| You can try to send other messages from ``ivyprobe``, for example:

- the following message will be received by our python agent: "Hello you", "Hello you and all", even "Hello " (with a trailing whitespace);
- but these messages won't be sent to our python agent: "Hello" (no trailing whitespace), or "I say Hello World"

Using groups in regexps
+++++++++++++++++++++++

We now know how to subscribe to message with regexps, but what if we want to get it would be more interesting if we could get back the interesting parts of a message.

| Suppose we want to monitor the change of status of a set of doors.  You have an equipment monitoring all doors, issuing message like ``status change: door <DOOR_ID>: <open|close>``.
| We want to listen to such message, so we take advantage of *groups* within regexps, i.e. parts of a regexps that are surrounded by the ``(`` and ``)`` metacharacters.
| An example being worth a thousand words, let's write it:

.. code-block:: python
   :name: tuto_register_subscription_door_status_args

   >>> def on_door_status(agent, door, status):
   ...     print("Agent %s: door %s status is: %s"%(agent, door, status)
   ...
   >>> IvyBindMsg(on_door_status, "status change: door ([^ ]*): (open|close)")
   2

Now if you send such a message from ``ivyprobe``::

   status change: door MAIN_ENTRANCE: open

our python agent's callback ``on_door_status()`` is called and prints::

  Agent pyivyprobe@localhost: door MAIN_ENTRANCE status is: open

Please note that:

- the callback always receives the sending agent as its first parameter,
- it also receives as many additional parameters as groups in the regexp supplied to ``IvyBindMsg``, supplied to the callback in the same order as in the subscription regexp.

In fact, it is completely possible to supply a generic callback such as this one:

  >>> def generic_callback(*args):
  ...   agent = args[0]
  ...   args = args[1:]
  ...   print(("Agent %s sent a matching message " +
  ...          "with %i arguments: %s")%(agent,len(args),str(args)))



Sending messages
----------------

First, let's remember that ``ivyprobe`` was launched at the very beginning of this tutorial with this command::

    $ ivyprobe.py -s hi 'ivyprobe (.*)'

By doing this, we already made two subscriptions for it. We can ask it to print them:

.. code-block:: python
   :caption: ``ivyprobe``

   .regexps
   Our subscriptions: 0:'hi', 1:'ivyprobe (.*)'

To send a message, one use ```IvySendMsg()``, let's send 3 messages:

.. code-block:: python
   :name: tuto_send_messages
   :linenos:

    >>> IvySendMsg('hi there')
    0
    >>> IvySendMsg('hi')
    1
    >>> IvySendMsg('ivyprobe are you here?')
    1

| Each call returns the number of agents to which a message was sent.
| As expected:

- the first message was sent to no-one (lines 1-2),
- the two subsequent ones were sent to 1 agent (lines 3-4 and 5-6), namely ``ivyprobe``

And ivyprobe acknowledges these messages by printing:

.. code-block:: python
   :caption: ``ivyprobe``

   Received from 127.0.0.1:xxxxx (my_agent): <no args>
   Received from 127.0.0.1:xxxxx (my_agent): ('are you here?',)

Examining the bus
-----------------

Here is how you can get the list of agents registered on the bus, and how to get informations on them:

.. code-block:: python
   :name: tuto_examine_bus

    >>> IvyGetApplicationList()
    ['pyivyprobe']
    >>> ivyprobe=IvyGetApplication('pyivyprobe')
    >>> IvyGetApplicationHost(ivyprobe)
    'localhost'
    >>> IvyGetApplicationName(ivyprobe) # may be useful in a callback
    'pyivyprobe'
    >>> IvyGetApplicationMessages(ivyprobe)
    [(0, 'hi'), (1, 'ivyprobe (.*)')]

.. note:: the 'agent' object that each callback receives as its first parameter is a :py:class:`ivy.ivy.IvyClient` object, just like the one returned by :py:func:`ivy.std_api.IvyGetApplication()` used above.

Terminating an agent
--------------------

While terminating an agent abruptly will be detected by the other agents on the bus, it is recommended that an agent call :py:func:`ivy.std_api.IvyStop` before exiting.  This notifies the other participants on the bus that it signs off, and it also properly terminates the python threads that were started when joining the bus (:py:func:`ivy.std_api.IvyStart`).


Summary
-------

We have seen here how to create and connect on agent to the default Ivy bus, how to choose the message to be received, how those message are handled upon reception, and how to send messages to others.


Going further
-------------

The standard API allows you to send direct messages to application, and offers a facility to manipulate timers. In it fully documented in the :doc:`ivy.std_api`.

Other source of informations:

- The ``ivyprobe`` utility source code can be found in ``example/ivyprobe.py``, it is built using the std_api.

- The document :doc:`ivy` also contains useful informations

- Obviously, the documentation found at the `Ivy Home Page <https://www.eei.cena.fr/products/ivy/>`_ will provide more context and technical informations, including the original whitepaper. And there is a `mailing-list <https://www.eei.cena.fr/products/ivy/contact.shtml>`_ where you can find help and experience from authors and other users
