from typing import List

from server.db.session import with_session
import uuid
from server.db.models.conversation_model import ConversationModel


@with_session
def add_conversation_to_db(session, chat_type, name="", conversation_id=None) -> ConversationModel:
    """
    新增聊天记录
    """
    if not conversation_id:
        conversation_id = uuid.uuid4().hex
    c = ConversationModel(id=conversation_id, chat_type=chat_type, name=name)

    session.add(c)
    session.commit()
    return c


@with_session
def get_all_conversation(session) -> List[ConversationModel]:
    """
    获取所有会话
    """
    return session.query(ConversationModel).all()


@with_session
def get_conversation_by_id(session, conversation_id: str) -> ConversationModel:
    """
    获取指定会话
    """
    return session.query(ConversationModel).filter_by(id=conversation_id).first()


@with_session
def del_conversation_by_id(session, conversation_id: str):
    """
    删除指定会话
    """
    session.query(ConversationModel).filter_by(id=conversation_id).delete()
    session.commit()


@with_session
def del_conversation_by_name(session, name: str):
    """
    删除指定会话
    """
    session.query(ConversationModel).filter_by(name=name).delete()
    session.commit()


if __name__ == '__main__':
    # id = add_conversation_to_db(chat_type="LLM", name="default")
    conversation_list = get_all_conversation()
    asd = {conv.id: conv.name for conv in conversation_list}
