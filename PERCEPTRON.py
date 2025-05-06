#PERCEPTRON

def activation(y_in):
    if y_in > 0:
        return 1
    elif y_in < 0:
        return -1
    else:
        return 0

def perceptron_train(data, w1, w2, bias, learning_rate=1, epochs=4):
    for epoch in range(1, epochs + 1):
        print(f"\nEpoch {epoch}")
        errors = 0
        for (x1, x2), target in data:
            y_in = x1 * w1 + x2 * w2 + bias
            output = activation(y_in)

            if output != target:
                w1 += learning_rate * target * x1
                w2 += learning_rate * target * x2
                bias += learning_rate * target
                errors += 1

            print(f"x1={x1}, x2={x2}, target={target}, output={output}, w1={w1}, w2={w2}, bias={bias}")

        if errors == 0:
            print("Training converged early.")
            break

    return w1, w2, bias

# Example use
if _name_ == "_main_":
    data = [
        ([1, 1], 1),
        ([1, -1], -1),
        ([-1, 1], -1),
        ([-1, -1], -1)
    ]

    w1 = float(input("Enter initial weight w1: "))
    w2 = float(input("Enter initial weight w2: "))
    bias = float(input("Enter initial bias: "))

    final_w1, final_w2, final_bias = perceptron_train(data, w1, w2, bias)
    print(f"\nFinal weights: w1={final_w1}, w2={final_w2}, bias={final_bias}")
