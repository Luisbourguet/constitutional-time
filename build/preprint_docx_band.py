import sys
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
src, out, status, title = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
hsuffix = sys.argv[5] if len(sys.argv) > 5 else ''
RED, BG = 'B03A2E', 'FDF0EC'
d = Document(src)
BYNAME = {st.name: st for st in d.styles}
for name in ['Title','Subtitle','Abstract Title','TOC Heading','Author','Date'] + [f'Heading {i}' for i in range(1,10)]:
    st = BYNAME.get(name)
    if st is None: continue
    rpr = st.element.get_or_add_rPr()
    for c in rpr.findall(qn('w:color')): rpr.remove(c)
    st.font.color.rgb = RGBColor(0,0,0)
for name in ['Body Text','First Paragraph','Abstract','Bibliography','Block Text','Image Caption','Table Caption']:
    if name in BYNAME: BYNAME[name].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement('w:shd'); shd.set(qn('w:val'),'clear'); shd.set(qn('w:color'),'auto'); shd.set(qn('w:fill'),fill); tcPr.append(shd)
def margins(cell):
    tcPr = cell._tc.get_or_add_tcPr(); m = OxmlElement('w:tcMar')
    for k,v in (('top',80),('bottom',80),('left',140),('right',140)):
        e = OxmlElement(f'w:{k}'); e.set(qn('w:w'),str(v)); e.set(qn('w:type'),'dxa'); m.append(e)
    tcPr.append(m)
tbl = d.add_table(rows=1, cols=2); tbl.alignment = WD_TABLE_ALIGNMENT.CENTER; tbl.autofit = False
tblPr = tbl._tbl.tblPr; borders = OxmlElement('w:tblBorders')
for e in ('top','left','bottom','right','insideV'):
    el = OxmlElement(f'w:{e}'); el.set(qn('w:val'),'single'); el.set(qn('w:sz'),'8'); el.set(qn('w:space'),'0'); el.set(qn('w:color'),RED); borders.append(el)
tblPr.append(borders); layout = OxmlElement('w:tblLayout'); layout.set(qn('w:type'),'fixed'); tblPr.append(layout)
widths = (Cm(2.8), Cm(13.7)); left, right = tbl.rows[0].cells
for c,w in zip((left,right),widths): c.width = w; c.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER; margins(c)
for gc,w in zip(tbl._tbl.tblGrid.findall(qn('w:gridCol')),widths): gc.set(qn('w:w'),str(int(w/635)))
shade(left,RED); shade(right,BG)
lp = left.paragraphs[0]; lp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = lp.add_run('PREPRINT'); r.bold=True; r.font.size=Pt(10.5); r.font.color.rgb=RGBColor(255,255,255)
rp = right.paragraphs[0]; r = rp.add_run(status); r.bold=True; r.font.size=Pt(9); r.font.color.rgb=RGBColor(0xB0,0x3A,0x2E)
first = d.paragraphs[0]; first._p.addprevious(tbl._tbl); sp = first.insert_paragraph_before(); sp.paragraph_format.space_after = Pt(6)
for sec in d.sections:
    hp = sec.header.paragraphs[0] if sec.header.paragraphs else sec.header.add_paragraph(); hp.text=''
    hr = hp.add_run('PREPRINT · not yet peer reviewed · November 2026' + hsuffix); hr.font.size=Pt(8); hr.font.color.rgb=RGBColor(0xB0,0x3A,0x2E); hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
for shp in d.inline_shapes:
    r_ = shp.width/shp.height; shp.width = Cm(16); shp.height = int(Cm(16)/r_)
cp = d.core_properties; cp.author='Luis Bourguet'; cp.title=title; cp.last_modified_by='Luis Bourguet'
d.save(out); print('saved', out)
