"""updates meal_type

Revision ID: 2e0fd6f1d1a8
Revises: a168d6f4de04
Create Date: 2024-08-07 10:59:42.211190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e0fd6f1d1a8'
down_revision = 'a168d6f4de04'
branch_labels = None
depends_on = None


# def upgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     with op.batch_alter_table('nutrition_logs', schema=None) as batch_op:
#         batch_op.alter_column('meal_type',
#                existing_type=sa.VARCHAR(),
#                type_=sa.Enum('BREAKFAST', 'LUNCH', 'DINNER', 'SNACK', name='mealtype'),
#                existing_nullable=False)
        
    
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nutrition_logs', schema=None) as batch_op:
        # First, change the column to text
        batch_op.alter_column(
            'meal_type',
            type_=sa.Text(),
            existing_type=sa.Enum('BREAKFAST', 'LUNCH', 'DINNER', 'SNACK', name='mealtype'),
            existing_nullable=False,
            postgresql_using='meal_type::text'
        )
        # Then, change the column to VARCHAR with a length limit if needed
        batch_op.alter_column(
            'meal_type',
            type_=sa.VARCHAR(length=255),
            existing_type=sa.Text(),
            existing_nullable=False
        )


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('nutrition_logs', schema=None) as batch_op:
        batch_op.alter_column('meal_type',
               existing_type=sa.Enum('BREAKFAST', 'LUNCH', 'DINNER', 'SNACK', name='mealtype'),
               type_=sa.VARCHAR(),
               existing_nullable=False)

    # ### end Alembic commands ###
