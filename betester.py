# vim: ts=4:sw=4
from errbot import botcmd, BotPlugin
from errbot.backends.base import Identifier, MUCRoom


class BackendTester(BotPlugin):
    """Those are commands to test a backend."""

    @botcmd
    def private(self, mess, args):
        """Send this command from a private channel.
        """
        if not isinstance(mess.frm, Identifier):
            yield "FAILED mess.frm is not an identifier"

        if not isinstance(mess.to, Identifier):
            yield "FAILED mess.to is not an identifier"

        if mess.to != self._bot.bot_identifier:
            yield "FAILED mess.to should implement equal correctly and resolve to the bot"

        if mess.to != self.build_identifier(str(mess.to)):
            yield "FAILED self.build_identifier(str(mess.to)) should be mess.to"

        if mess.frm != self.build_identifier(str(mess.frm)):
            yield "FAILED self.build_identifier(str(mess.frm)) should be mess.frm"
        yield "End of test"

    @botcmd
    def public(self, mess, args):
        """Send this command from a public channel.
        """
        if not isinstance(mess.frm, Identifier):
            yield "FAILED mess.frm is not an Identifier"

        if not isinstance(mess.to, MUCRoom):
            yield "FAILED mess.to is not a MUCRoom"

        if mess.to != self.query_room(str(mess.to)):
            yield "FAILED self.query_room(str(mess.to)) should be mess.to"

        if mess.frm != self.build_identifier(str(mess.frm)):
            yield "FAILED self.build_identifier(str(mess.frm)) should be mess.frm"
        yield "End of test"

