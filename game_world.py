world = [[] for _ in range(4)]
collision_pairs = {}

def add_collision_pair(group, a, b):
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [[], []]
    # 중복 추가 방지
    if a and a not in collision_pairs[group][0]:
        collision_pairs[group][0].append(a)
    if b and b not in collision_pairs[group][1]:
        collision_pairs[group][1].append(b)

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

def handle_collisions():
    for group, pairs in collision_pairs.items():
        # 복사본을 순회하여 충돌 처리 중 목록 변경에도 안전
        for a in list(pairs[0]):
            for b in list(pairs[1]):
                if collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)


def add_object(o, depth = 0):
    world[depth].append(o)


def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
    pass

def remove_object(o):
    # 레이어에서 제거 시도
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            return
    # 레이어에 없어도 충돌 목록에서 제거만 하고 조용히 반환
    remove_collision_object(o)
    return


def clear():
    for layer in world:
        layer.clear()
    collision_pairs.clear()
