ValueError : Constraint must have a name 오류 발생 시

flask db heads -> 최종 리비전 보기
b580e4d830e0 (head)

flask db current -> 현재 리비전 보기
INFO ~~~~~ SQLiteImpl.
INFO ~~~~~ DDL.
c0b3b3bf5bcb

flask db stamp heads -> 현재 리비전을 최종 리비전으로 변경
INFO ~~~~ SQliteImpl.
INFO ~~~~ DDL.
INFO ~~~~ b580e4d830e0 -> c0b3b3bf5bcb

flask db migrate
Generation ~~~~~ c0b3b3bf5bcb_.py ... done

myproject/migrations/versions/c0b3b3bf5bcb_.py open
아래 내용 수정
def upgrade():
        #batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key('user_id', 'user', ['user_id'], ['id'], ondelete='CASCADE')
위와 같이 foreign_key(None 을 foreign_key('user_id' 로 수정

flask db upgrade
INFO ~~~~ SQLiteImple.
INFO ~~~~ DDL.
INFO ~~~~ b580e4d830e0 -> c0b3b3bf5bcb, empty message