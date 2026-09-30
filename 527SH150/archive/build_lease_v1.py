#!/usr/bin/env python3
"""Build the 527 Hwy 150 room rental agreement as Markdown and PDF from one content list."""
import pathlib, datetime as dt
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak

OUT = pathlib.Path(__file__).resolve().parent.parent / "527 HWY 150"
BASENAME = "Room Rental Agreement - 527 Hwy 150 - FINAL"

# Content: list of (kind, text). kinds: title, subtitle, h, p, li, sig, table, pagebreak
C = []
def title(t): C.append(("title", t))
def sub(t): C.append(("subtitle", t))
def h(t): C.append(("h", t))
def p(t): C.append(("p", t))
def li(t): C.append(("li", t))
def table(rows): C.append(("table", rows))
def pb(): C.append(("pagebreak", ""))

title("ROOM RENTAL AGREEMENT")
sub("Shared Housing, Owner-Occupied. 527 State Route 150, Arroyo Seco, New Mexico 87514")

p("This Room Rental Agreement (\"Agreement\") is made on September 28, 2026, between <b>Susan Nelson</b> (\"Owner\") and <b>David S. Paul</b> (\"Tenant\"). Owner and Tenant will share the house. This Agreement is governed by the New Mexico Uniform Owner-Resident Relations Act, NMSA 1978, Sections 47-8-1 through 47-8-52 (the \"Act\"). Where this Agreement is silent, the Act controls. Owner will give Tenant a signed copy of this Agreement.")

h("1. Parties and Property")
p("<b>Owner:</b> Susan Nelson, owner of record of the house at 527 State Route 150, Arroyo Seco, NM 87514 (the \"Premises\"). Owner lives at the Premises. Owner is the person authorized to manage the Premises and to receive notices on Owner's behalf (Act, Section 47-8-19). Owner's contact: 527 State Route 150, Arroyo Seco, NM 87514; email suzienelson007@gmail.com; phone 575-770-8039.")
p("<b>Tenant:</b> David S. Paul. Tenant's contact: email stupaul22@gmail.com; phone 720-275-1350. Tenant may use the Premises address as Tenant's residence address for mail, driver's license, voter registration and similar purposes.")

h("2. What Is Rented")
p("<b>Exclusive use by Tenant:</b>")
li("The <b>front bedroom</b> (\"Tenant's Room\").")
li("The <b>private bathroom</b> on the same side of the house as Tenant's Room.")
p("<b>Shared or designated use by Tenant:</b>")
li("The <b>back bedroom</b>, for Tenant's desk and as a workspace. Owner keeps access to the back bedroom; Tenant's desk and work materials may stay there for the term.")
li("A <b>designated storage space in the garage</b> for Tenant's belongings and equipment.")
li("The kitchen, living areas, laundry, yard, and other common areas, shared with Owner.")
li("<b>One parking space</b> at the Premises for Tenant's vehicle. Tenant and Owner will share shoveling of the walkway and parking area after storms. If Owner arranges plowing of the driveway, plowing is at Owner's expense.")

h("3. Term")
p("<b>Fixed Term:</b> six months, from <b>November 1, 2026</b> through <b>April 30, 2027</b>.")
p("<b>After the Fixed Term:</b> beginning May 1, 2027, this Agreement continues automatically <b>month to month on the same terms</b> unless either party ends it. During the month-to-month period, either party may end the tenancy by giving the other <b>written notice at least 30 days before the next rent due date</b>, consistent with Section 47-8-37 of the Act.")
p("Except as provided in Section 8 (Early Termination) or for a breach handled under the Act, neither party may end the tenancy during the Fixed Term.")

h("4. Rent")
p("<b>Rent is $800.00 per month</b>, plus the <b>flat utility fee of $25.00 per month</b> described in Section 5, for a <b>total monthly payment of $825.00</b>, due on or before the <b>1st day of each month</b>.")
p("Payment method: Zelle. Owner will provide a receipt on request.")
p("<b>Late fee:</b> $50.00 if the monthly payment is not received by the <b>10th day of the month</b>. (This is below the 10 percent cap in Section 47-8-15(D) of the Act.)")
p("<b>No rent increase during the Fixed Term.</b> Rent and the utility fee will not increase before May 1, 2027. During any month-to-month period, Owner may change the rent or utility fee only by written notice given at least 30 days before the rent due date on which the change takes effect, consistent with Section 47-8-15(F) of the Act.")

h("5. Utilities")
p("The $25.00 monthly utility fee is a <b>flat fee</b> that covers Tenant's share of <b>internet, gas or propane (including heat), electricity, water, trash, and sewer</b>. There is no cap, no separate metering, and no additional utility billing to Tenant. Owner keeps all utility accounts in Owner's name and pays the providers. Tenant agrees to use reasonable conservation (for example, not leaving heat on high with windows open).")

h("6. Security Deposit and Prepaid Last Month's Rent")
p("<b>Security deposit: $200.00</b>, paid by Tenant on <b>September 26, 2026</b>. Owner holds the deposit under Section 47-8-18 of the Act. Within <b>30 days</b> after the tenancy ends and Tenant moves out, Owner will return the deposit, less any lawful deductions, together with a <b>written itemized statement</b> of any deductions. Ordinary wear and tear is not deductible. The deposit is not rent, and Tenant may not apply it to rent.")
p("<b>Prepaid last month's rent: $800.00</b>, paid by Tenant on September 28, 2026. This amount is prepaid rent for <b>April 2027</b>, the final month of the Fixed Term, and will be credited to April 2027 rent (Tenant will pay only the $25.00 utility fee for April 2027). If the tenancy ends earlier under Section 8 or by written agreement, the prepaid amount is credited to Tenant's final month of occupancy, and any unused portion is refunded with the deposit accounting. If the tenancy continues month to month, the prepaid amount is applied to April 2027 as stated and rent for May 2027 onward is paid normally.")

h("7. Move-In Condition")
p("Before or at move-in, Owner and Tenant will walk through Tenant's Room, the bathroom, the back bedroom desk area, the garage storage space, and the common areas together, record their condition and any furnishings on <b>Exhibit A</b>, take photographs, and both sign Exhibit A. Exhibit A is part of this Agreement. Deductions from the deposit are limited to damage beyond ordinary wear that is not already recorded on Exhibit A.")

h("8. Early Termination for Major Life Changes")
p("The parties recognize that six months is a real commitment and that life happens. During the Fixed Term, <b>either party may end this Agreement with at least 30 days' written notice</b> if any of the following occurs:")
li("Tenant's employment or primary income requires Tenant to relocate more than 100 miles from the Premises;")
li("Serious illness, injury, or death of Tenant or Owner, or of a member of either party's immediate family, that makes continuing the arrangement impractical;")
li("Owner sells, or contracts to sell, the Premises, or the Premises become uninhabitable;")
li("Any other major change in circumstances that both parties agree in writing makes continuing unreasonable.")
p("If this Section is used, Tenant owes rent and the utility fee only through the end of the 30-day notice period, with no other early termination fee. The prepaid April rent is credited to the final month or refunded as described in Section 6, and the deposit is handled under Section 6. Nothing in this Section limits either party's rights under the Act.")

h("9. Privacy and Entry")
p("Tenant's Room and the private bathroom are Tenant's private space. Owner will not enter Tenant's Room or bathroom except <b>(a)</b> with at least <b>24 hours' notice</b>, at a reasonable time, for repairs, inspection, or showing, or <b>(b)</b> in an emergency, consistent with Section 47-8-24 of the Act. Owner will not move or remove Tenant's belongings from the back bedroom desk area or garage storage space without asking first.")

h("10. Pet")
p("Tenant's dog <b>Granite</b>, a 70-pound Weimaraner, is permitted to live at the Premises for the entire tenancy. No additional pet deposit or pet fee is charged. Granite may remain in the house unattended while Tenant is out for the day. Tenant is responsible for Granite's behavior, waste, and any damage Granite causes beyond ordinary wear, and will keep Granite under control on the Premises. Owner's consent to Granite may not be withdrawn during the tenancy as long as Tenant meets these responsibilities.")

h("11. Household Rules")
li("<b>Cleanliness:</b> Each party will keep their own bedroom and bathroom, as well as the common areas, appliances, fixtures and furnishings they use, clean and in good condition, and will clean up after using the kitchen and laundry.")
li("<b>Overnight guests:</b> Allowed. Tenant will give Owner a heads-up in advance, and guests may stay <b>no longer than two consecutive nights at a time</b>. Tenant is responsible for Tenant's guests.")
li("<b>Quiet hours:</b> <b>9:00 PM to 7:00 AM</b>. Both parties will keep noise to a reasonable level during quiet hours.")
li("<b>Smoking:</b> No smoking or vaping inside the house or garage.")
li("<b>Alterations:</b> Tenant may hang pictures and small fixtures in Tenant's Room using small nails or hooks and will patch holes on move-out. No other alterations without Owner's written consent.")
li("<b>Shared costs:</b> Household consumables shared by both parties (for example, dish soap, paper goods) will be handled by mutual agreement.")

h("12. Maintenance and Repairs")
p("Owner will maintain the Premises as required by Section 47-8-20 of the Act, including the structure, heating, plumbing, electrical, water and hot water, and any appliances Owner supplies. Tenant will promptly report anything that needs repair, will use the Premises reasonably, and will pay for damage caused by Tenant, Tenant's guests, or Granite beyond ordinary wear. Tenant may use the garage storage space for storage and quiet hobby work with hand tools that does not create fire risk, fumes, or noise during quiet hours.")

h("13. Insurance")
p("Owner's homeowner's insurance does not cover Tenant's personal property. Tenant may carry renter's insurance but is not required to.")

h("14. Communication and Notices")
p("Owner and Tenant will check in briefly once a month about how the shared house is working. Routine matters may be handled by text or email. Notices of termination, breach, or other notices under the Act must be in writing and delivered in person, by mail, or by email to the addresses in Section 1 (or updated addresses given in writing).")

h("15. General Terms")
li("<b>Governing law:</b> This Agreement is governed by the laws of the State of New Mexico, including the Act.")
li("<b>Severability:</b> If any provision is unenforceable in whole or in part, the remaining provisions continue in full force.")
li("<b>Amendments:</b> This Agreement may be changed only by a written amendment signed by both parties.")
li("<b>Entire agreement:</b> This Agreement, with Exhibit A, is the whole agreement between the parties about the Premises and replaces the earlier draft dated September 28, 2026.")
li("<b>Copies:</b> Each party will receive a signed copy.")

C.append(("sig", ""))
pb()
h("EXHIBIT A: Move-In Condition Report and Furnishings")
p("Completed together by Owner and Tenant at move-in. Attach photographs (note the number taken). Both parties sign.")
table([
    ["Area", "Condition at move-in (note any damage)", "Furnishings present"],
    ["Front bedroom (Tenant's Room)", "", ""],
    ["Private bathroom", "", ""],
    ["Back bedroom (desk area)", "", ""],
    ["Garage storage space", "", ""],
    ["Kitchen and appliances", "", ""],
    ["Living areas", "", ""],
    ["Laundry", "", ""],
    ["Yard and parking", "", ""],
    ["Keys received: house ____ bedroom ____ other ____", "", ""],
    ["Photographs taken: ______ (date: ______)", "", ""],
])
C.append(("sig", "exhibit"))

# ---------------- Markdown ----------------
def strip_tags(t):
    return t.replace("<b>", "**").replace("</b>", "**")
md = []
for kind, t in C:
    if kind == "title": md += [f"# {t}", ""]
    elif kind == "subtitle": md += [f"*{t}*", ""]
    elif kind == "h": md += [f"## {t}", ""]
    elif kind == "p": md += [strip_tags(t), ""]
    elif kind == "li": md += [f"- {strip_tags(t)}"]
    elif kind == "table":
        md += ["| " + " | ".join(t[0]) + " |", "|" + "---|" * len(t[0])]
        for r in t[1:]: md.append("| " + " | ".join(c if c else " " for c in r) + " |")
        md.append("")
    elif kind == "pagebreak": md += ["", "---", ""]
    elif kind == "sig":
        md += ["", "## Signatures" if t == "" else "### Exhibit A Signatures", "",
               "| | Name | Signature | Date |", "|---|---|---|---|",
               "| Owner | Susan Nelson | ______________________ | ________ |",
               "| Tenant | David S. Paul | ______________________ | ________ |", ""]
# fix list spacing: ensure blank line after a run of li
out = []
for i, line in enumerate(md):
    out.append(line)
    if line.startswith("- ") and (i + 1 >= len(md) or not md[i + 1].startswith("- ")):
        out.append("")
(OUT / f"{BASENAME}.md").write_text("\n".join(out).replace("\n\n\n", "\n\n") + "\n")

# ---------------- PDF ----------------
styles = getSampleStyleSheet()
base = ParagraphStyle("base", parent=styles["Normal"], fontName="Times-Roman", fontSize=11, leading=14.5, spaceAfter=6)
st = {
    "title": ParagraphStyle("t", parent=base, fontName="Times-Bold", fontSize=16, leading=20, alignment=1, spaceAfter=2),
    "subtitle": ParagraphStyle("s", parent=base, fontName="Times-Italic", fontSize=10.5, alignment=1, spaceAfter=14),
    "h": ParagraphStyle("h", parent=base, fontName="Times-Bold", fontSize=12, spaceBefore=10, spaceAfter=4),
    "p": base,
    "li": ParagraphStyle("li", parent=base, leftIndent=18, bulletIndent=6, spaceAfter=3),
}
story = []
for kind, t in C:
    if kind in ("title", "subtitle", "h", "p"):
        story.append(Paragraph(t, st[kind]))
    elif kind == "li":
        story.append(Paragraph(t, st["li"], bulletText="•"))
    elif kind == "table":
        tb = Table([[Paragraph(c, base) for c in r] for r in t], colWidths=[2.3*inch, 2.6*inch, 1.6*inch], rowHeights=[34] + [40]*(len(t)-1), repeatRows=1)
        tb.setStyle(TableStyle([("GRID", (0,0), (-1,-1), 0.5, colors.black),
                                ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#e8e8e8")),
                                ("VALIGN", (0,0), (-1,-1), "TOP"),
                                ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white]),
                                ]))
        story += [Spacer(1, 6), tb, Spacer(1, 10)]
    elif kind == "pagebreak":
        story.append(PageBreak())
    elif kind == "sig":
        rows = [["", "Name", "Signature", "Date"],
                ["Owner", "Susan Nelson", "", ""],
                ["Tenant", "David S. Paul", "", ""]]
        tb = Table(rows, colWidths=[0.8*inch, 1.6*inch, 2.8*inch, 1.3*inch], rowHeights=[18, 34, 34])
        tb.setStyle(TableStyle([("FONT", (0,0), (-1,-1), "Times-Roman", 11),
                                ("FONT", (0,0), (-1,0), "Times-Bold", 11),
                                ("LINEBELOW", (2,1), (3,-1), 0.7, colors.black),
                                ("VALIGN", (0,0), (-1,-1), "BOTTOM"),
                                ("BOTTOMPADDING", (0,0), (-1,-1), 4)]))
        story += [Spacer(1, 12), Paragraph("Signatures" if t == "" else "Exhibit A Signatures", st["h"]), KeepTogether(tb)]

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Roman", 8.5)
    canvas.drawString(inch, 0.6*inch, "Room Rental Agreement, 527 State Route 150, Arroyo Seco, NM")
    canvas.drawRightString(letter[0]-inch, 0.6*inch, f"Page {doc.page}    Owner initials ____  Tenant initials ____")
    canvas.restoreState()

doc = SimpleDocTemplate(str(OUT / f"{BASENAME}.pdf"), pagesize=letter, leftMargin=inch, rightMargin=inch, topMargin=0.9*inch, bottomMargin=0.9*inch,
                        title="Room Rental Agreement 527 State Route 150", author="Susan Nelson and David S. Paul")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("wrote", OUT / f"{BASENAME}.md", "and .pdf")
