import os.path
import glob
import configparser
import importlib

import bankparser


class BankConfig:

    bank = None

    @staticmethod
    def get_list_banks():
        """
        Return list avalible banks
        :return:
        """
        moddir = os.path.dirname(__file__)
        path_banks = os.path.join(moddir, 'banks')
        mask = os.path.join(path_banks, "*.py")
        listbanks = []
        for file in glob.glob(mask):
            pyfile = os.path.basename(file)
            bank = os.path.splitext(pyfile)[0]
            listbanks.append(bank)
        return listbanks

    def _read_ini(self):
        """
        Read user settings for bank from ini files in ~/.bankparser
        banks.ini - common setting for all banks
        'bankname'.ini - current bank
        :return:
        """
        inifile = self.bank.bankname + '.ini'
        common_ini_file = 'banks.ini'
        inifiles = []
        userpath = os.path.expanduser('~/.bankparser')
        progpath = os.path.realpath(__file__)
        # common ini file
        inifiles.append(os.path.join(userpath, common_ini_file))
        inifiles.append(os.path.join(progpath, common_ini_file))
        # current bank ini file
        inifiles.append(os.path.join(userpath, inifile))
        inifiles.append(os.path.join(progpath, inifile))

        settings = configparser.ConfigParser()
        settings.optionxform = str
        settings.read(inifiles, encoding='utf-8')

        for section in settings.sections():
                maplist = {}
                for key in settings[section]:
                    maplist[key] = settings[section][key]
                setattr(self.bank, 'm_' + section, maplist)

    def get_parser(self, bankname):
        """
        Return parser class for bankname - ParserCSV or ParserXML
        :param bankname:
        :return:
        """
        self.read_bank(bankname)
        parser = getattr(bankparser, self.bank.parser)
        return parser

    def read_bank(self, bankname):
        """
        Read settings of bank
        :param bankname:
        :return:
        """
        if ((not self.bank) or (self.bank.bankname != bankname)) and (bankname != '__init__'):
            modbank = importlib.import_module("bankparser.banks." + bankname)
            if not modbank:
                print('Не найден py файл')
                raise FileNotFoundError("Не найден файл .py для банка {}".format(bankname))
            bankcls = getattr(modbank, 'Bank')
            self.bank = bankcls()
            self.bank.bankname = bankname
            self._read_ini()

bankconfig = BankConfig()


def get_bank_config(bankname):
    bankconfig.read_bank(bankname)
    return bankconfig
