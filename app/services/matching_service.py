from sqlalchemy import func, or_
from ..extensions import db
from ..models import Item, Match

def simple_candidates_for_lost(lost_id, limit=10):
    lost = db.session.get(Item, lost_id)
    if not lost or lost.item_type != "lost":
        return []
    # คัดของพบ (found) ที่คล้าย title/color/brand และพื้นที่ใกล้เคียง (ถ้ามีพิกัด)
    q = db.select(Item).filter(Item.item_type=="found", Item.status=="open")
    if lost.brand: q = q.filter(Item.brand.ilike(f"%{lost.brand}%"))
    like = f"%{lost.title.split()[0]}%"
    q = q.filter(or_(Item.title.ilike(like), Item.description.ilike(like)))
    # คะแนนอย่างง่าย: ใช้ความคล้ายข้อความ + ระยะที่ประมาณด้วย city/district เท่านั้น (ให้เริ่มง่าย)
    results = db.session.scalars(q.limit(limit)).all()
    # แปลงเป็นรายการ (item, score)
    scored = []
    for it in results:
        score = 0
        if lost.color and it.color and lost.color.lower() in it.color.lower():
            score += 0.2
        if lost.brand and it.brand and lost.brand.lower() in it.brand.lower():
            score += 0.2
        if lost.city and it.city and lost.city == it.city:
            score += 0.2
        if lost.district and it.district and lost.district == it.district:
            score += 0.2
        if lost.title and it.title and lost.title.split()[0].lower() in it.title.lower():
            score += 0.2
        scored.append((it, round(min(score, 1.0),2)))
    return sorted(scored, key=lambda x: x[1], reverse=True)
