
PLATFORM_SELECTION_LIST = ('None','SLE78', 'SLC52', 'Pxyz')
INTERFACE_SELECTION_LIST = ('CB', 'CL')
SCP_SELECTION_LIST = ('02', '03')
TEST_KEYS_SELECTION_LIST = ('none', 'VISA test keys fix', 'VISA test keys derived','from JLoad key file')
LCS_SELECTION_LIST = ('OP_READY', 'INITIALIZED', 'SECURED', 'CARD_LOCKED')

def emptyIfNone(s):
    return '' if s is None else s

def noneIfEmpty(s):
    s = s.strip()
    return None if s == '' else s
    
class TestCardSettings(object):
    
    def __init__(self, platform = None, interface = None, flashImage = None, scp = None, testKeys = None, lcs = None, imageFileName=None, keyFileName = None, capFileName = None, scriptFileName = None, printFileName = None):
        self.platform = PLATFORM_SELECTION_LIST[0] if platform is None else platform
        self.interface = INTERFACE_SELECTION_LIST[0] if interface is None else interface
        self.scp = SCP_SELECTION_LIST[0] if scp is None else scp
        self.testKeys = TEST_KEYS_SELECTION_LIST[0] if testKeys is None else testKeys
        self.lcs = LCS_SELECTION_LIST[0] if lcs is None else lcs
        self.imageFileName = imageFileName
        self.keyFileName = keyFileName
        self.capFileName = capFileName
        self.scriptFileName = scriptFileName 
        self.printFileName = printFileName 
        #self.verifyValidity()        


    def print(self):
        print('  platform:       %s' % self.platform)
        print('  scp:            %s' % self.scp)
        print('  lcs:            %s' % self.lcs)
        print('  testKeys:       %s' % self.testKeys)
        print('  interface:      %s' % self.interface)
        print('  keyFileName:    %s' % self.keyFileName)
        print('  imageFileName:  %s' % self.imageFileName)
        print('  capFileName:    %s' % self.capFileName)
        print('  scriptFileName: %s' % self.scriptFileName)
        print('  printFileName:  %s' % self.printFileName)
        
        
    def load(self, fileName):
        with open(fileName, 'rt') as f:
            for l in f:
                l = l.strip()
                if   l.startswith('platform: '):       self.platform = noneIfEmpty(l[10:])
                elif l.startswith('scp: '):            self.scp = noneIfEmpty(l[5:])
                elif l.startswith('lcs: '):            self.lcs = noneIfEmpty(l[5:])
                elif l.startswith('testKeys: '):       self.testKeys = noneIfEmpty(l[10:])
                elif l.startswith('interface: '):      self.interface = noneIfEmpty(l[11:])
                elif l.startswith('keyFileName: '):    self.keyFileName = noneIfEmpty(l[13:])
                elif l.startswith('imageFileName: '):  self.imageFileName = noneIfEmpty(l[15:])
                elif l.startswith('capFileName: '):    self.capFileName = noneIfEmpty(l[13:])
                elif l.startswith('scriptFileName: '): self.scriptFileName = noneIfEmpty(l[16:])
                elif l.startswith('printFileName: '):  self.printFileName = noneIfEmpty(l[14:])
            
    def save(self, fileName):
        with open(fileName, 'wt') as f:
            save_file = { 'platform: %s'        % emptyIfNone(self.platform),
                          'scp: %s'             % emptyIfNone(self.scp),
                          'lcs: %s'             % emptyIfNone(self.lcs),
                          'testKeys: %s'        % emptyIfNone(self.testKeys),
                          'interface: %s'       % emptyIfNone(self.interface),
                          'keyFileName: %s'     % emptyIfNone(self.keyFileName),
                          'imageFileName: %s'   % emptyIfNone(self.imageFileName),
                          'capFileName: %s'     % emptyIfNone(self.capFileName),
                          'scriptFileName: %s'  % emptyIfNone(self.scriptFileName),
                          'printFileName: %s'   % emptyIfNone(self.printFileName)
            }
            f.writelines("%s\n" % line for line in save_file)            
