# -*- mode: python -*-
# filename = Main.spec

block_cipher = None

a = Analysis(['main.py'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             cipher=block_cipher)
pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='program',
          debug=False,
          strip=None,
          upx=True,
          console=True,
          runtime_tmpdir=None)
app = BUNDLE(exe)
