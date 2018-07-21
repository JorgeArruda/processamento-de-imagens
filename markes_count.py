if len(markers.shape) == 2:
        a = 0
        for x in range(markers.shape[0]):
            for y in range(markers.shape[1]):
                if markers[x, y] > 0:
                    a += 1
                    # print(markers[x, y])

        print('A = ', a, '  Tamanho = ', markers.shape[0]*markers.shape[1])
    meu = watershedd(gradiente_inverso, markers)
    if len(meu.shape) == 2:
        a = 0
        for x in range(meu.shape[0]):
            for y in range(meu.shape[1]):
                if meu[x, y] > 0:
                    a += 1
                    # print(meu[x, y])

        print('Meu A = ', a, '  Tamanho = ', meu.shape[0]*meu.shape[1])
    cv2.imshow('Meu alg', meu)