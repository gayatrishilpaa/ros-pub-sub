# ROS2 Publisher-Subscriber

A basic ROS2 project demonstrating communication between two nodes using the Publisher-Subscriber model.

The project consists of a **Talker Node** that continuously publishes messages to a topic and a **Listener Node** that subscribes to the same topic and prints the received messages to the terminal.

**ROS2 Version:** Humble

---

## Concepts Used

* Python
* `rclpy`
* `std_msgs/String`
* Publishers
* Subscribers
* Topics
* Timers

---

## Features

* The **Talker Node** publishes the message `Hello everyone <count>`.
* The message counter starts at **0** and increments after every published message.
* Messages are published every **0.5 seconds**.
* The publisher node runs continuously using `rclpy.spin()`.
* The **Listener Node** subscribes to the same topic and displays the received messages in the terminal.

---

## System Design

| Talker Node                 | Topic    | Listener Node              |
| --------------------------- | -------- | -------------------------- |
| Creates a Publisher         | `/topic` | Creates a Subscription     |
| Publishes `String` messages | →        | Receives `String` messages |
| `timer_callback()`          | →        | `listener_callback()`      |

---

## How to Run

1. Build the workspace.

```bash
colcon build
```

2. Source the workspace.

```bash
source install/setup.bash
```

3. Run the Talker Node.

```bash
ros2 run <package_name> talker_node
```

4. Open a new terminal, source the workspace again, and run the Listener Node.

```bash
ros2 run <package_name> listener_node
```

---

## Notes

* Ensure `package.xml` and `setup.py` are updated with the correct package and executable names before building the workspace.
