# vim: ts=4:sw=4
from errbot import botcmd, BotPlugin
from errbot.backends.base import Person, Room, RoomOccupant


class BackendTester(BotPlugin):
    """Those are commands to test a backend."""

    @botcmd
    def private(self, mess, args):
        """Send this command from a private channel.
        """
        if not isinstance(mess.frm, Person):
            yield "FAILED mess.frm is not a Person"

        if not isinstance(mess.to, Person):
            yield "FAILED mess.to is not a Person"

        if mess.to != self._bot.bot_identifier:
            yield "FAILED mess.to should implement equal correctly and resolve to the bot"

        if mess.to != self.build_identifier(str(mess.to)):
            yield "FAILED self.build_identifier(str(mess.to)) should be mess.to"

        if mess.frm != self.build_identifier(str(mess.frm)):
            yield "FAILED self.build_identifier(str(mess.frm)) should be mess.frm"
        
        # Test if identifiers resist being pickled.
        try:
            self['mess.frm'] = mess.frm
            if mess.frm != self['mess.frm']:
                yield "FAILED mess.frm is different from its pickled version"
        except Exception as e:
            yield "FAILED storing mess.frm resulted in an exception %e" % e

        try:
            self['mess.to'] = mess.to
            if mess.to != self['mess.to']:
                yield "FAILED mess.to is different from its pickled version"
        except Exception as e:
            yield "FAILED storing mess.to resulted in an exception %e" % e

        yield "End of test"

    @botcmd
    def public(self, mess, args):
        """Send this command from a public channel.
        """
        if not isinstance(mess.frm, Person):
            yield "FAILED mess.frm is not a Person"

        if not isinstance(mess.frm, RoomOccupant):
            yield "FAILED mess.frm is not a RoomOccupant"

        if not isinstance(mess.frm.room, Room):
            yield "FAILED mess.frm.room is not a Room"

        if not isinstance(mess.to, Room):
            yield "FAILED mess.to is not a Room"

        if mess.to != self.query_room(str(mess.to)):
            yield "FAILED self.query_room(str(mess.to)) should be mess.to"

        if mess.to != self.build_identifier(str(mess.to)):
            yield "FAILED self.build_identifier(str(mess.to)) should be mess.to"

        if not isinstance(self.build_identifier(str(mess.to)), Room):
            yield "FAILED self.build_identifier(str(mess.to)) should be a Room"

        if mess.frm != self.build_identifier(str(mess.frm)):
            yield "FAILED self.build_identifier(str(mess.frm)) should be mess.frm"
        
        try:
            self['mess.frm'] = mess.frm
            if mess.frm != self['mess.frm']:
                yield "FAILED mess.frm is different from its pickled version"
        except Exception as e:
            yield "FAILED storing mess.frm resulted in an exception %e" % e

        try:
            self['mess.to'] = mess.to
            if mess.to != self['mess.to']:
                yield "FAILED mess.to is different from its pickled version"
        except Exception as e:
            yield "FAILED storing mess.to resulted in an exception %e" % e

        yield "End of test"

