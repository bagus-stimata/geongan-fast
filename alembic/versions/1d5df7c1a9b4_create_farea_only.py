from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "<ISI_REV_BARU>"
down_revision = None  # karena kita stamp ke base
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "farea",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("kode1", sa.String(length=20), nullable=False, server_default=""),
        sa.Column("kode2", sa.String(length=20), nullable=False, server_default=""),
        sa.Column("description", sa.String(length=100), nullable=False, server_default=""),
        sa.Column("fdivisionBean", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("statusActive", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        sa.Column("fregionBean", sa.Integer(), nullable=True, server_default="0"),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.Column("modified", sa.DateTime(), nullable=True),
        sa.Column("modifiedBy", sa.String(length=30), nullable=True, server_default=""),
    )
    op.create_index("ix_farea_id", "farea", ["id"])

def downgrade():
    op.drop_index("ix_farea_id", table_name="farea")
    op.drop_table("farea")