import random

WORD_LEN = 5      # 단어 길이
MAX_TRIES = 6     # 최대 시도 횟수

# 추측 대상 단어 목록
WORD_LIST = [
    "apple", "brain", "smart", "money", "place",
    "water", "light", "sound", "house", "train",
    "sugar", "plant", "heart", "north", "south",
    "world", "dream", "smile", "music", "voice"
]

def choose_word():
    """단어 목록에서 랜덤으로 하나 선택"""
    return random.choice(WORD_LIST)

def check_guess(secret, guess):
    """
    한 번의 추측 결과를 분석해서 힌트 문자열을 반환
    secret : 정답 단어
    guess  : 사용자가 입력한 단어
    반환값 : 'O', '?', '_' 로 구성된 문자열
    """
    result = ['_'] * WORD_LEN
    used = [False] * WORD_LEN  # 정답 단어에서 이미 매칭에 사용했는지

    # 1차: 위치/글자 모두 맞는 경우
    for i in range(WORD_LEN):
        if guess[i] == secret[i]:
            result[i] = 'O'
            used[i] = True

    # 2차: 글자는 있지만 위치만 다른 경우
    for i in range(WORD_LEN):
        if result[i] == 'O':
            continue  # 이미 맞춘 위치는 건너뜀

        for j in range(WORD_LEN):
            if not used[j] and guess[i] == secret[j]:
                result[i] = '?'
                used[j] = True
                break

    return "".join(result)

def main():
    secret = choose_word()
    tries = 0
    success = False

    print("=== Wordle 스타일 콘솔 미니게임 (Python) ===")
    print(f"- {WORD_LEN}글자 영어 단어를 맞춰보세요.")
    print(f"- 최대 {MAX_TRIES}번까지 시도할 수 있습니다.\n")

    while tries < MAX_TRIES:
        guess = input(f"[{tries+1}/{MAX_TRIES}] 추측할 단어 입력 ({WORD_LEN}글자): ")
        guess = guess.strip().lower()  # 대소문자 구분 안 하려면 사용

        if len(guess) != WORD_LEN:
            print(f"⚠ 정확히 {WORD_LEN}글자를 입력해야 합니다.\n")
            continue

        tries += 1

        hint = check_guess(secret, guess)
        print(f"시도 {tries}: {guess} -> {hint}")

        if guess == secret:
            success = True
            break

        print()

    if success:
        print(f"\n🎉 정답입니다! 단어는 \"{secret}\" 였습니다.")
        print(f"총 {tries}번 만에 맞췄어요!")
    else:
        print("\n기회를 모두 사용했습니다... 😢")
        print(f"정답은 \"{secret}\" 였습니다.")

if __name__ == "__main__":
    main()
