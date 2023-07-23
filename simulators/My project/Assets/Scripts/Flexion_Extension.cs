using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Flexion_Extension : MonoBehaviour
{
    //software control variables
    public GameObject settings;
    public Button start;
    public bool running = false;

    //hand body parts class implementation
    public class handMethods
    {
        public Transform hand_rig;
        public Transform wrist;
        public Transform hand;
        public Transform thumb;
        public Transform index_finger;
        public Transform middle_finger;
        public Transform ring_finger;
        public Transform little_finger;
        private string left_right;
        public float thumb_speed;
        public float other_speed;

        public handMethods(GameObject which_hand, string l_r)
        {
            hand_rig = which_hand.transform.GetChild(0);
            wrist = hand_rig.GetChild(0);
            hand = wrist.GetChild(0);
            thumb = hand.GetChild(0);
            index_finger = hand.GetChild(1);
            middle_finger = hand.GetChild(2);
            ring_finger = hand.GetChild(3);
            little_finger = hand.GetChild(4);
            left_right = l_r;
            if(left_right == "right")
            {
                thumb_speed = (float) -1;
                other_speed = (float) 1.2;
            }
            if(left_right == "left")
            {
                thumb_speed = (float) -1;
                other_speed = (float) -1.2;
            }
        }

        public void flexion()
        {
            thumb.transform.Rotate(0, 0, thumb_speed, Space.Self);
            index_finger.Rotate((float) other_speed, 0, 0, Space.Self);
            middle_finger.Rotate((float) other_speed, 0, 0, Space.Self);
            ring_finger.Rotate((float) other_speed, 0, 0, Space.Self);
            little_finger.Rotate((float) other_speed, 0, 0, Space.Self);
        }

        public void extension()
        {
            thumb.transform.Rotate(0, 0, (-1)*thumb_speed, Space.Self);
            index_finger.Rotate((float) ((-1)* other_speed), 0, 0, Space.Self);
            middle_finger.Rotate((float) ((-1) * other_speed), 0, 0, Space.Self);
            ring_finger.Rotate((float) ((-1) * other_speed), 0, 0, Space.Self);
            little_finger.Rotate((float) ((-1) * other_speed), 0, 0, Space.Self);
        }
    }

    //body parts declaration
    public GameObject right_hand;
    public GameObject left_hand;
    private handMethods right_hand_methods;
    private handMethods left_hand_methods;


    // On click start button, enable body parts GameObjects and disable settings screen 
    void startButtonClick()
    {
        if (running == false)
        {
            settings.SetActive(false);
            right_hand.SetActive(true);
            left_hand.SetActive(true);
            running = true;
        }
    }






    //App running

    // Start is called before the first frame update
    void Start()
    {
        settings.SetActive(true);
        right_hand.SetActive(false);
        left_hand.SetActive(false);
        start.onClick.AddListener(startButtonClick);
        right_hand_methods = new handMethods(right_hand, "right");
        left_hand_methods = new handMethods(left_hand, "left");
}

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKey(KeyCode.UpArrow))
        {
            right_hand_methods.flexion();
            left_hand_methods.flexion();
        }
        if (Input.GetKey(KeyCode.DownArrow))
        {
            right_hand_methods.extension();
            left_hand_methods.extension();
        }
        
    }
}