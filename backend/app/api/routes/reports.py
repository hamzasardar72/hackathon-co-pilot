from fastapi import APIRouter
from fastapi.responses import Response
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

router = APIRouter()


@router.get("/download")
def download_report():
    buffer = []

    def build_report():
        pdf = SimpleDocTemplate("claimwise_report.pdf", pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        story.append(Paragraph("ClaimWise AI Assessment Report", styles["Title"]))
        story.append(Spacer(1, 16))
        story.append(Paragraph("Claim ID: CLM-1001", styles["BodyText"]))
        story.append(Paragraph("Claimant: Ava Thompson", styles["BodyText"]))
        story.append(Paragraph("Damage Severity: Moderate", styles["BodyText"]))
        story.append(Paragraph("Confidence Score: 0.93", styles["BodyText"]))
        story.append(Spacer(1, 12))
        table_data = [["Metric", "Value"], ["Classification", "Vehicle Damage"], ["Recommended Action", "Pending Review"]]
        table = Table(table_data)
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#133a5e")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                    ("GRID", (0, 0), (-1, -1), 1, colors.grey),
                ]
            )
        )
        story.append(table)
        pdf.build(story)

    build_report()

    with open("claimwise_report.pdf", "rb") as file:
        file_bytes = file.read()

    return Response(content=file_bytes, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=claimwise_report.pdf"})
