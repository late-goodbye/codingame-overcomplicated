import unittest
from easy.disordered_first_contact.disordered_first_contact import Message, Coder


class TestMessage(unittest.TestCase):

    def test_text(self):
        test_message = 'test_message'
        message = Message(test_message)
        self.assertEqual(message.text, test_message)
        self.assertEqual(message.__repr__(), test_message)
        self.assertIsNone(Message().text)
        self.assertIsNone(Message().__repr__())


class TestCoder(unittest.TestCase):

    def setUp(self):
        self.coder = Coder()

    def test_encode_message(self):
        message = Message('hello world')
        self.coder.transform(message, -1)
        self.assertEqual(message.text, 'worlelhlo d')

        message = Message('hello worlds')
        self.coder.transform(message, -6)
        self.assertEqual(message.text, 'hrlellwo ods')

        message = Message('abcdefghi')
        self.coder.transform(message, -1)
        self.assertEqual(message.text, 'ghibcadef')

        message = Message('this is a mutliple encoded text')
        self.coder.transform(message, -5)
        self.assertEqual(message.text, 'hitoeplmu eneicldts aide  tsxt ')

    def test_decode_message(self):
        message = Message('ghibcadef')
        self.coder.transform(message, 1)
        self.assertEqual(message.text, 'abcdefghi')

        message = Message('hitoeplmu eneicldts aide  tsxt ')
        self.coder.transform(message, 5)
        self.assertEqual(message.text, 'this is a mutliple encoded text')

    def test_long_string(self):
        message = Message(' rius lorem. Duis risus nunc, condimentum at metun lacinia id. Pellentebortis. '
                          'Suspendttis sed , maxis ornare nipulvinar. In v aliquam erat maximus bibenetus neque, '
                          'tempus lovarius ipsnare vel. Donec , vitae sx enim. Sed vitaes sed nei ipFusces t. '
                          'e at sum. Alt nibhgittidisse eu eteger id cursumque vel dui et libs.Maecenash. '
                          'Suspendisse tristiqueeu condcondimentum atec orDui sitipsuorLem m dolteger quismus eget i '
                          'ssim lacuss. Suspum feron arcu idvinar id eula elit in effiuspenlor. in blandem solm ne i '
                          'psuc lorlicitudit ut acSIn luctus vcitur vae pulat arcu ferment maximus. '
                          'Integerendisse hendrim. Inmentum nibh non dum.  amet, tur adlit. Fusceci pretium iacsi ut '
                          'felibm neque, quis dignis orligsx nec sagi aliquam do maximuaodo nulla. isi quis, '
                          'iquam esdu, npretium comMauris as. Ins elitque a mattittis. Morbi volutpat eroegestas irit '
                          'vel ante ac dignisss nes scing elitconsecteoripi. Quisque msagiel puruuli mollis n enim '
                          'est, ac bibendumissmentum. Ut dictum mi vel luctus rhoncus.tempor id.')
        self.coder.transform(message, 3)
        self.assertEqual(message.text,
                         'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque metus neque, sagittis sed '
                         'condimentum at, maximus eget elit. Fusce condimentum nibh non erat maximus bibendum. Duis '
                         'ornare nisi ut felis aliquam pulvinar. In vel purus nec orci pretium iaculis. Suspendisse '
                         'hendrerit vel ante ac dignissim. Integer quis mollis nibh. Suspendisse tristique enim est, '
                         'ac bibendum metus ornare vel. Donec egestas non arcu id maximus. Integer varius ipsum '
                         'neque, quis dignissim lacus lacinia id. Pellentesque vel dui et libero tempus lobortis. '
                         'Suspendisse pulvinar id ex nec sagittis. Morbi volutpat ligula at arcu fermentum fermentum. '
                         'Ut maximus sed neque a mattis.Maecenas dictum mi vel luctus rhoncus. Suspendisse eu ex '
                         'enim. Sed vitae aliquam dolor. In luctus velit in efficitur varius. Integer id cursus elit, '
                         'vitae sagittis lorem. Duis risus nunc, condimentum at nisi quis, pretium commodo nulla. '
                         'Mauris a ipsum nec lorem sollicitudin blandit ut ac est. Fusce at dui ipsum. Aliquam est '
                         'nibh, tempor id.')
